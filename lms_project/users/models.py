from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('trainer','Trainer'),
    ('student', 'Student')
]



class CustomUserManager(BaseUserManager):
    def create_user(self, email, role, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,role='admin',password=None):
        user = self.create_user(email=email,role=role,password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRES_FIELDS = ['role']


    def __str__(self):
        return self.email
