from django.contrib.auth import authenticate, get_user_model

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework_jwt.settings import api_settings

from .permissions import AnonPermissionOnly, IsOwnerOrReadOnly
from .serializers import UserRegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()


class APIAuthView(APIView):
    permission_classes = [AnonPermissionOnly, IsOwnerOrReadOnly]

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'detail': 'You are already authenticated'}, status=400)
        username = request.data.get('username')
        password = request.data.get('password')
        qs = User.objects.filter(email__iexact=username).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token, user, request=request)
                return Response(response, status=200)
        return Response({"details": "Invalid Credentials"}, status=401)


class APIRegisterView(CreateAPIView):
    permission_classes = [AnonPermissionOnly]
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


# class APIRegisterView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return Response({'detail': 'You are already authenticated and registered!'}, status=400)
#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#         email = request.data.get('email')
#         password = request.data.get('password')
#         password2 = request.data.get('password')
#         is_active = request.data.get('is_active')
#
#         qs = User.objects.filter(email__iexact=email)
#         if password != password2:
#             Response({"details": "Password have to match."}, status=401)
#         if qs.exists():
#             return Response({"details": "User already exists"}, status=401)
#         else:
#             user = User.objects.create(first_name=first_name, last_name=last_name, email=email)
#             user.set_password(password)
#             user.is_active = False
#             user.save()
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             response = jwt_response_payload_handler(token, user, request=request)
#             # return Response(response, status=201)
#             return Response({"detail": "Thank for your registering. Please confirm your email."}, status=201)
