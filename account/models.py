from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, company_name, phone, password=None):
        if not email:
            raise ValueError("Email is required")
        if not company_name:
            raise ValueError("Company name is required")
        if not phone:
            raise ValueError("An active phone number is required")

        user = self.model(
            email=self.normalize_email(email),
            company_name=company_name,
            phone = phone
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, company_name, phone, password=None):
            user = self.create_user(
                email = email,
                company_name=company_name,
                phone=phone,
                password=password
            )
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
            user.save(using=self._db)
            return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name = "email addresss", max_length=100, unique=True)
    company_name = models.CharField(verbose_name="company name", max_length=200, unique=True)
    phone = models.CharField(verbose_name="company phone", max_length=20)
    date_joined = models.DateField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateField(verbose_name="last login", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=['company_name','phone']
    objects=MyUserManager()

    def __str__(self):
        return self.company_name

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

