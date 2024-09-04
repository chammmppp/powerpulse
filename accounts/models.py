from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.


#  model
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("Email address is required")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)  # hash รหัสผ่านก่อนที่จะบันทึกลงฐานข้อมูล
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # Because this is the superuser then we've given the permission to it
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Account model
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)  # Property
    last_name = models.CharField(max_length=50)  # Property
    email = models.EmailField(max_length=100, unique=True)  # Property
    phone_number = models.CharField(max_length=10, blank=True, null=True)  # Property

    # Required
    date_joined = models.DateTimeField(auto_now_add=True)  # Property
    last_login = models.DateTimeField(auto_now=True, null=False)  # Property
    is_admin = models.BooleanField(default=False)  # Property
    is_staff = models.BooleanField(default=False)  # Property
    is_active = models.BooleanField(default=True)  # Property
    is_superuser = models.BooleanField(default=False)  # Property

    USERNAME_FIELD = (
        "email"  # This attribute will be used as unique identifier for the user
    )
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]  # This attribute will be prompted during the creation of a superuser

    objects = MyAccountManager()  # Object of the class Account

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
