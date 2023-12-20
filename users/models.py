from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from .validators import validate_phone_number
from .managers import CustomUserManager


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True, db_index=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    join_at = models.DateTimeField(auto_now_add=True)

    last_login = models.DateTimeField(auto_now=True)

    company = models.CharField(null=True)

    logo = models.ImageField(upload_to="users_logo/", null=True)

    phone_number = models.CharField(validators=[validate_phone_number], null=True)

    city = models.CharField(null=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()
