from django.contrib.auth.models import AbstractUser
from django.db import models


class TimeStampedMode(models.Model):
    """
    An abstract base class model that provides self-
    updating ''created'' and ''modified'' fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    can_sprinkle = models.BooleanField(default=False, help_text="User is able to sprinkle or not.")


class ModelFormFailuriHistory(models.Model):
    form_data = models.TextField()
    model_data = models.TextField()
