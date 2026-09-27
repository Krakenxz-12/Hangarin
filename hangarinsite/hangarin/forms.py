from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import (
    Task,
    Category,
    Priority,
    Note,
    SubTask,
)


class BootstrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            if isinstance(field.widget, forms.Select):
                field.widget.attrs["class"] = "form-select"

            else:
                field.widget.attrs["class"] = "form-control"


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class TaskForm(BootstrapModelForm):

    class Meta:
        model = Task

        fields = [
            "title",
            "description",
            "deadline",
            "status",
            "category",
            "priority",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Enter task description..."
                }
            ),

            "deadline": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),
        }


class CategoryForm(BootstrapModelForm):

    class Meta:
        model = Category

        fields = [
            "name",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter category name..."
                }
            ),
        }


class PriorityForm(BootstrapModelForm):

    class Meta:
        model = Priority

        fields = [
            "name",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter priority name..."
                }
            ),
        }


class NoteForm(BootstrapModelForm):

    class Meta:
        model = Note

        fields = [
            "task",
            "content",
        ]

        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Write your note..."
                }
            ),
        }


class SubTaskForm(BootstrapModelForm):

    class Meta:
        model = SubTask

        fields = [
            "parent_task",
            "title",
            "status",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Enter subtask title..."
                }
            ),
        }