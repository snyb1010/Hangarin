from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/create/", views.task_create, name="task_create"),
    path("tasks/<int:pk>/", views.task_detail, name="task_detail"),
    path("tasks/<int:pk>/edit/", views.task_update, name="task_update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task_delete"),
    path("tasks/<int:task_pk>/subtasks/create/", views.subtask_create, name="subtask_create"),
    path("subtasks/<int:pk>/edit/", views.subtask_update, name="subtask_update"),
    path("subtasks/<int:pk>/delete/", views.subtask_delete, name="subtask_delete"),
    path("tasks/<int:task_pk>/notes/create/", views.note_create, name="note_create"),
    path("notes/<int:pk>/edit/", views.note_update, name="note_update"),
    path("notes/<int:pk>/delete/", views.note_delete, name="note_delete"),
]
