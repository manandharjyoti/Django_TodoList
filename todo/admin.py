from django.contrib import admin
from todo.models import Task
from django.db import models



@admin.register(Task)

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description","date", "priority", "user")

    


