from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.forms import TaskForm
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    ordering = [
        "is_done",
        "-created_at",
    ]
    queryset = Task.objects.prefetch_related("tags").order_by(
        "is_done", "-created_at"
    )


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TagListView(ListView):
    model = Tag
    ordering = ["name"]


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


def toggle_task_status(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()

    return HttpResponseRedirect(reverse_lazy("tasks:index"))
