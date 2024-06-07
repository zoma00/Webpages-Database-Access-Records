from django.contrib.auth.models  import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    # Add your custom fields and methods here

    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')

    class Meta:
        # Remove swappable attribute for non-swappable model
        # swappable = 'AUTH_USER_MODEL'
        pass


