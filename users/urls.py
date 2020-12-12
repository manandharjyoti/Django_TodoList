
from django.contrib import admin
from django.urls import path, include
from users.views import signup,login_view,logout_view
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name =  'users'
urlpatterns = [
path('signup/',signup, name="signup"),
path('login_view/',login_view, name="login_view"),
path('logout_view/',logout_view, name="logout_view"),
]