from django.forms import ModelForm
from django import forms
from .models import Task, Category, Priority, Note, SubTask


class TaskForm(ModelForm):

    class Meta:
        model = Task

        fields = ["title", "description", "deadline", "status", "category", "priority",]


class CategoryForm(ModelForm):

    class Meta:
        model = Category

        fields = ["name",]


class PriorityForm(ModelForm):

    class Meta:
        model = Priority

        fields = ["name",]


class NoteForm(ModelForm):

    class Meta:
        model = Note

        fields = ["task", "content", ]


class SubTaskForm(ModelForm):

    class Meta:
        model = SubTask

        fields = ["parent_task", "title", "status",]