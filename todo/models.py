from django.db import models
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User



class Task(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null = True, blank = True)
    date = models.DateField(auto_now = False, auto_now_add = False)
    Priority = (("low", "low"), ("medium" ,"medium"), ("high" ,"high"))
    priority = models.CharField(max_length=255, blank=True, null=True, choices=Priority)
    


    def __str__(self):
        return self.title

    

# Create your models here.
