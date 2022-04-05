from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    My shiny user model.
    Add extra custom fields there if needed

    my_extra_field_name = models.ImageField(...)
    """
