from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, CreateView, View
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url
from django.utils.safestring import mark_safe
from django.contrib.messages.views import SuccessMessageMixin, messages

from .forms import UserLoginForm, UserRegistrationForm, ReactivateEmailFrom
from .models.email_activation import EmailActivation


# Create your views here.
class RequestFormAttachMixin(object):
    def get_form_kwargs(self):
        kwargs = super(RequestFormAttachMixin, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class NextUrlMixin(object):
    default_next = '/'

    def get_next_url(self):
        next_ = self.request.GET.get('next')
        next_post = self.request.POST.get('next')
        redirect_path = next_ or next_post or None
        if is_safe_url(redirect_path, self.request.get_host()):
            return redirect_path
        return self.default_next


class UserLoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = UserLoginForm
    success_url = '/profile/'
    default_next = '/profile/'
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context['title'] = 'Login'
        return context


class UserRegistrationView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_message = 'Registration successful. We send activation instruction on your email.'
    success_url = '/account/login/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data(**kwargs)
        context['title'] = 'Registration'
        return context


class AccountEmailActivateView(FormMixin, View):
    success_url = '/account/login/'
    form_class = ReactivateEmailFrom
    key = None

    def get(self, request, key=None, *args, **kwargs):
        if key is not None:
            qs = EmailActivation.objects.filter(key__iexact=key)
            confirm_qs = qs.conformable()
            if confirm_qs.count() == 1:
                obj = confirm_qs.first()
                obj.activate()
                messages.success(self.request, "Your email has been confirmed. You can login now.")
                return redirect('login')
            else:
                activated_qs = qs.filter(key__iexact=key, activated=True)
                if activated_qs.exists():
                    reset_link = reverse('password_reset')
                    msg = """Your email has already confirmed!
                    Did you mean <a href="{link}">reset your password</a>?
                    """.format(link=reset_link)
                    messages.info(self.request, mark_safe(msg))
                    return redirect('login')
        context = {
            'form': self.get_form(),
            'key': self.key
        }
        return render(self.request, 'registration/activation_error.html', context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        msg = "Your account activation link sent. Please check your email."
        messages.success(self.request, msg)
        email = form.cleaned_data.get("email")
        obj = EmailActivation.objects.email_exists(email).first()
        user = obj.user
        new_activation = EmailActivation.objects.create(user=user, email=email)
        new_activation.send_activation()
        return super(AccountEmailActivateView, self).form_valid(form)

    def form_invalid(self, form):
        context = {
            "form": form,
            "key": self.key
        }
        return render(self.request, 'registration/activation_error.html', context)


def get_logout(request):
    logout(request)
    return redirect('home')
