from django.contrib import admin
from .models import CustomUser

# Register the CustomUser model in the Django admin interface
admin.site.register(CustomUser)
