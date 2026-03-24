from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm, SubTaskForm, TaskForm
from .models import Note, SubTask, Task


def home(request):
	query = request.GET.get("q", "").strip()
	sort = request.GET.get("sort", "newest")

	tasks = Task.objects.select_related("priority", "category").annotate(
		subtask_count=Count("subtask", distinct=True),
		note_count=Count("note", distinct=True),
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

	order_by_map = {
		"newest": "-created_at",
		"oldest": "created_at",
		"deadline": "deadline",
		"title": "title",
	}
	tasks = tasks.order_by(order_by_map.get(sort, "-created_at"))

	paginator = Paginator(tasks, 8)
	page_obj = paginator.get_page(request.GET.get("page"))

	context = {
		"page_obj": page_obj,
		"tasks": page_obj.object_list,
		"query": query,
		"sort": sort,
		"total_tasks": Task.objects.count(),
		"completed_tasks": Task.objects.filter(status=Task.Status.COMPLETED).count(),
		"in_progress_tasks": Task.objects.filter(status=Task.Status.IN_PROGRESS).count(),
		"pending_tasks": Task.objects.filter(status=Task.Status.PENDING).count(),
		"total_subtasks": SubTask.objects.count(),
		"total_notes": Note.objects.count(),
	}
	return render(request, "tasks/home.html", context)


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


def subtask_create(request, task_pk):
	task = get_object_or_404(Task, pk=task_pk)
	form = SubTaskForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		subtask = form.save(commit=False)
		subtask.task = task
		subtask.save()
		return redirect("tasks:task_detail", pk=task.pk)
	return render(request, "tasks/subtask_form.html", {"form": form, "task": task, "is_create": True})


def subtask_update(request, pk):
	subtask = get_object_or_404(SubTask.objects.select_related("task"), pk=pk)
	form = SubTaskForm(request.POST or None, instance=subtask)
	if request.method == "POST" and form.is_valid():
		form.save()
		return redirect("tasks:task_detail", pk=subtask.task.pk)
	return render(
		request,
		"tasks/subtask_form.html",
		{"form": form, "task": subtask.task, "subtask": subtask, "is_create": False},
	)


def subtask_delete(request, pk):
	subtask = get_object_or_404(SubTask.objects.select_related("task"), pk=pk)
	task_pk = subtask.task.pk
	if request.method == "POST":
		subtask.delete()
		return redirect("tasks:task_detail", pk=task_pk)
	return render(request, "tasks/subtask_confirm_delete.html", {"subtask": subtask})


def note_create(request, task_pk):
	task = get_object_or_404(Task, pk=task_pk)
	form = NoteForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		note = form.save(commit=False)
		note.task = task
		note.save()
		return redirect("tasks:task_detail", pk=task.pk)
	return render(request, "tasks/note_form.html", {"form": form, "task": task, "is_create": True})


def note_update(request, pk):
	note = get_object_or_404(Note.objects.select_related("task"), pk=pk)
	form = NoteForm(request.POST or None, instance=note)
	if request.method == "POST" and form.is_valid():
		form.save()
		return redirect("tasks:task_detail", pk=note.task.pk)
	return render(
		request,
		"tasks/note_form.html",
		{"form": form, "task": note.task, "note": note, "is_create": False},
	)


def note_delete(request, pk):
	note = get_object_or_404(Note.objects.select_related("task"), pk=pk)
	task_pk = note.task.pk
	if request.method == "POST":
		note.delete()
		return redirect("tasks:task_detail", pk=task_pk)
	return render(request, "tasks/note_confirm_delete.html", {"note": note})
