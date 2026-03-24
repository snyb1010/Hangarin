from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def home(request):
	query = request.GET.get("q", "").strip()
	tasks = (
		Task.objects.select_related("priority", "category")
		.annotate(subtask_count=Count("subtask"), note_count=Count("note"))
		.order_by("-created_at")
	)

	if query:
		tasks = tasks.filter(
			Q(title__icontains=query)
			| Q(description__icontains=query)
			| Q(status__icontains=query)
			| Q(priority__name__icontains=query)
			| Q(category__name__icontains=query)
			| Q(subtask__title__icontains=query)
			| Q(note__content__icontains=query)
		).distinct()

	return render(request, "tasks/home.html", {"tasks": tasks, "query": query})


def task_create(request):
	form = TaskForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		task = form.save()
		return redirect("tasks:task_detail", pk=task.pk)
	return render(request, "tasks/task_form.html", {"form": form, "is_create": True})


def task_detail(request, pk):
	task = get_object_or_404(
		Task.objects.select_related("priority", "category").prefetch_related("subtask_set", "note_set"),
		pk=pk,
	)
	return render(request, "tasks/task_detail.html", {"task": task})


def task_update(request, pk):
	task = get_object_or_404(Task, pk=pk)
	form = TaskForm(request.POST or None, instance=task)
	if request.method == "POST" and form.is_valid():
		task = form.save()
		return redirect("tasks:task_detail", pk=task.pk)
	return render(request, "tasks/task_form.html", {"form": form, "task": task, "is_create": False})


def task_delete(request, pk):
	task = get_object_or_404(Task, pk=pk)
	if request.method == "POST":
		task.delete()
		return redirect("tasks:home")
	return render(request, "tasks/task_confirm_delete.html", {"task": task})
