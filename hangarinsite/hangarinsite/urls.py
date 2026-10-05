"""
URL configuration for hangarinsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from hangarin.views import UserLoginView, UserLogoutView, RegisterView, ProfileView, ProfileUpdateView, SettingsView
from hangarin.views import HomePageView, TaskCreateView, TaskDeleteView, TaskList, TaskUpdateView, CategoryList, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, PriorityList, PriorityCreateView, PriorityUpdateView, PriorityDeleteView, NoteList, NoteCreateView, NoteUpdateView, NoteDeleteView, SubTaskList, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView, ProfileView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", HomePageView.as_view(), name="home"), 
    path('', include('pwa.urls')),

    path("tasks/", TaskList.as_view(), name="task-list"),
    path("tasks/add/", TaskCreateView.as_view(),  name="task-add"),
    path("tasks/<int:pk>/edit/",TaskUpdateView.as_view(), name="task-edit"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(),name="task-delete"),

    path("categories/", CategoryList.as_view(), name="category-list"),
    path("categories/add/", CategoryCreateView.as_view(),  name="category-add"),
    path("categories/<int:pk>/edit/",CategoryUpdateView.as_view(), name="category-edit"),
    path("categories/<int:pk>/delete/", CategoryDeleteView.as_view(),name="category-delete"),

    path("priorities/", PriorityList.as_view(), name="prio-list"),
    path("priorities/add/", PriorityCreateView.as_view(),  name="prio-add"),
    path("priorities/<int:pk>/edit/",PriorityUpdateView.as_view(), name="prio-edit"),
    path("priorities/<int:pk>/delete/", PriorityDeleteView.as_view(),name="prio-delete"),

    path("notes/", NoteList.as_view(), name="note-list"),
    path("notes/add/", NoteCreateView.as_view(),  name="note-add"),
    path("notes/<int:pk>/edit/",NoteUpdateView.as_view(), name="note-edit"),
    path("notes/<int:pk>/delete/", NoteDeleteView.as_view(),name="note-delete"),

    path("subtasks/", SubTaskList.as_view(), name="subtask-list"),
    path("subtasks/add/", SubTaskCreateView.as_view(),  name="subtask-add"),
    path("subtasks/<int:pk>/edit/",SubTaskUpdateView.as_view(), name="subtask-edit"),
    path("subtasks/<int:pk>/delete/", SubTaskDeleteView.as_view(),name="subtask-delete"),

    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path("accounts/", include("allauth.urls")),

    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile-edit"),
    path("settings/", SettingsView.as_view(), name="settings"),
]
