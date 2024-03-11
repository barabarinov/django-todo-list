from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    ordering = ['-created_at', "is_done"]


class TaskCreateView(CreateView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task


class TaskDeleteView(DeleteView):
    model = Task


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag


class TagUpdateView(UpdateView):
    model = Tag


class TagDeleteView(DeleteView):
    model = Tag
