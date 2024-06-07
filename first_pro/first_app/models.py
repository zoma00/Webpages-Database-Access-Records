from django.db import models
from django.conf import settings
from accounts.models import CustomUser 

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name 

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Update the reference to AUTH_USER_MODEL

    def __str__(self):
        return f"{self.user} accessed {self.name} on {self.date}"

        

