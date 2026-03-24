"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from studentorg.views import (
    HomePageView,
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView,
    SubTaskListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView,
    NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PriorityListView, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
)
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('index.html', RedirectView.as_view(url='/', permanent=True)),
    path("accounts/", include("allauth.urls")),
    path('', views.HomePageView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('tasks/<pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('subtasks/', SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/add/', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtasks/<pk>/', SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtasks/<pk>/delete/', SubTaskDeleteView.as_view(), name='subtask-delete'),
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/add/', NoteCreateView.as_view(), name='note-add'),
    path('notes/<pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('notes/<pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('priorities/', PriorityListView.as_view(), name='priority-list'),
    path('priorities/add/', PriorityCreateView.as_view(), name='priority-add'),
    path('priorities/<pk>/', PriorityUpdateView.as_view(), name='priority-update'),
    path('priorities/<pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),
]
