from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid

class SpecialUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_verified = models.BooleanField(default=False)
    verification_token = models.UUIDField(default=uuid.uuid4, unique=True)
    is_special_user = models.BooleanField(default=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='special_users_set',  # Changed related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='special_users_set',  # Changed related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

