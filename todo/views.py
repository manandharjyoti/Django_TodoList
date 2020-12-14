from django.shortcuts import render, redirect, reverse
from todo.models import Task
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from todo.forms import TaskForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url="/users/login_view/")
def todolist_view(request):
    today = datetime.now().date()
    todolist = Task.objects.filter(user=request.user)
    # user = User.objects.all()
    context = {"todolist": todolist, "today": today}
    return render(request, "todolist.html", context)


@login_required(login_url="/users/login_view/")
def addlist_view(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        Task = form.save(commit=False)
        Task.user = request.user
        Task = Task.save()
        # form.save()
        # return HttpResponseRedirect()
        return redirect(reverse("todo:todolist_view"))
    else:
        form = TaskForm()
    return render(request, "form.html", {"form": form})


def delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect(reverse("todo:todolist_view"))


@login_required(login_url="/users/login_view/")
def edit_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("todo:todolist_view"))
    return render(request, "form.html", {"form": form})
