# Django Custom User Authentication (Django 2.1.3)

## Function
01. Customize Django Authentication
02. Customize User Login
03. Customize User Registration
04. Email Activation View
05. Email Reactivation
06. Login Form for Confirmation Emails
07. User Account Home
08. Naming and Dropdown
09. Password Change
10. Password Reset with email activation
11. Custom QuerySet for Confirmable Activations
12. You can easily create multiple users.

## SETUP Accounts App on Your Project.

First you have to install all requirements.txt. Set thid party module *widget_tweaks* in `INSTALLED_APPS` on your settings.py file.

Than you have to copy or move [accounts](https://github.com/jakiiii/django-custom-user-auth/tree/master/src/customuserauth/accounts) app.

After including accounts app in your project than go to your *settings.py* file.

Set this line.
`AUTH_USER_MODEL = 'accounts.User'`

Than set SMTP settings in settings.py file.

```
# SMTP GMAIL Settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''  # SET EMAIL
EMAIL_HOST_PASSWORD = ''  # SET PASSWORD OR APP PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Jqurity | Custom User Auth (jqurity@gmail.com)'
BASE_URL = ''  # SET YOUR BASE URL [BASE_URL = '127.0.0.1:8000']

MANAGERS = [
    ('set a name', 'set an email'),  # Just like ('khan', 'khan@gmail.com')
]

ADMINS = MANAGERS
```

When you set your email than you have to change your gmail account security.

* [Allow less secure apps](https://myaccount.google.com/lesssecureapps?pli=1) and
* [Disable Captcha](https://accounts.google.com/displayunlockcaptcha)

>OR

Your can set app password on gmail.
Here have instructions how to create app password.

[Sign in using App Passwords](https://support.google.com/accounts/answer/185833)

Now go to your mail urls.py file and set accounts realated urls. Befoure you have to include method.

>`from django.urls import path, include`

```
path('accounts/', RedirectView.as_view(url='/account')),
path('account/', include('accounts.urls'), name='account'),
path('accounts/', include('accounts.password.urls')),
```

After you have to go **main Templates** directory and you will see a registration folder. Copy or Cut that folder and set your project in **main Template** folder.

Than you have to migrate first than makemigration.
```
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
```

## SETUP Profile App on Your Project.

You can easily setup user profile app. Here have two built in methods method where user can change his Name and Password. You can create an profile app or copy past few lines of code.

Copy or cut profiles app [views.py](https://github.com/jakiiii/django-custom-user-auth/tree/master/src/customuserauth/profiles) and set your project.

Go your main *urls.py* file and setup profiles urls path.
```
    path('profiles/', RedirectView.as_view(url='/profile')),
    path('profile/', include('profiles.urls'), name='profile'),
```

**Multiple User**
You can easily create multiple user for your project. Go to User Model and set you users. Here few example.
```
class User(AbstractBaseUser):
    ...
    # is_student = models.BooleanField(default=False)
    # is_teacher = models.BooleanField(default=False)
    # is_management = models.BooleanField(default=False)
```

Process is done. Its a beta version. We will add more feature and fixing bug. It is an open source project. You can contribute this project or can share idea.

And I'm following *codingforentrepreneurs* tutorial for developing this project. Thnks for **Justin Mitchel**.
