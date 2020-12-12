from django.contrib import admin
from django.urls import path
from todo.views import todolist_view, addlist_view,delete_view,edit_view

app_name= "todo"

urlpatterns = [
  
    path('todolist_view/',todolist_view, name ="todolist_view"),
    path('addlist_view/',addlist_view, name ="addlist_view"),
    path('delete_view/<int:task_id>/', delete_view, name="delete_view"),
    path('edit_view/<int:task_id>/', edit_view, name="edit_view"),
    

]
