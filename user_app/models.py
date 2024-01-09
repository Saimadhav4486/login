# user_dashboard/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        related_query_name='customuser_group',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to these groups.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        related_query_name='customuser_permission',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def save(self, *args, **kwargs):
        if not self.pk:
            # Set is_patient or is_doctor based on the form used for signup
            if 'Patient' in self.__class__.__name__:
                self.is_patient = True
            elif 'Doctor' in self.__class__.__name__:
                self.is_doctor = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
