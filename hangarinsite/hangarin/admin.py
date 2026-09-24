from django.contrib import admin

from .models import (Priority, Category, Task, Note, SubTask)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "priority",
        "status",
        "deadline",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "status",
        "category",
        "priority",
    )


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "task",
        "content",
        "created_at",
    )

    search_fields = (
        "content",
        "task__title",
    )


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "parent_task",
        "status",
    )

    search_fields = (
        "title",
        "parent_task__title",
    )

    list_filter = (
        "status",
    )