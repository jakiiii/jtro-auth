from django.db import models

from .user_models import User


# Create your manager here.
class EmailActivationManager(models.Manager):
    pass


# Create your model here.
class EmailActivation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=32)
    key = models.CharField(max_length=120, null=True, blank=True)
    activated = models.BooleanField(default=False)
    forced_expired = models.BooleanField(default=False)
    expired = models.IntegerField(default=3)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    objects = EmailActivationManager()

    def __str__(self):
        return self.email
