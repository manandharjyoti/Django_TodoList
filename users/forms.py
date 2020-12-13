from django import forms
from todo.models import Task
from django.contrib.auth.forms import UserCreationForm, User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
