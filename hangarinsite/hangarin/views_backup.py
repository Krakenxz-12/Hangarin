from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import (
    Task,
    Category,
    Priority,
    Note,
    SubTask,
)

from .forms import (
    TaskForm,
    CategoryForm,
    PriorityForm,
    NoteForm,
    SubTaskForm,
)


class HomePageView(ListView):

    model = Task
    template_name = "home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["total_tasks"] = Task.objects.count()

        context["total_categories"] = Category.objects.count()

        context["total_priorities"] = Priority.objects.count()

        context["total_notes"] = Note.objects.count()

        context["total_subtasks"] = SubTask.objects.count()

        context["completed_tasks"] = Task.objects.filter(
            status="Completed"
        ).count()

        context["pending_tasks"] = Task.objects.filter(
            status="Pending"
        ).count()

        context["in_progress_tasks"] = Task.objects.filter(
            status="In Progress"
        ).count()

        return context

class TaskList(ListView):

    model = Task
    context_object_name = "task"
    template_name = "task_list.html"
    paginate_by = 5

    def get_queryset(self):

        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:

            qs = qs.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(status__icontains=query)
                | Q(category__name__icontains=query)
                | Q(priority__name__icontains=query)
            )

        return qs

    def get_ordering(self):

        allowed = [
            "title",
            "deadline",
            "status",
            "priority__name",
            "category__name",
        ]

        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "title"


class TaskCreateView(CreateView):

    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


class TaskUpdateView(UpdateView):

    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")


class TaskDeleteView(DeleteView):

    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task-list")


class CategoryList(ListView):

    model = Category
    context_object_name = "categories"
    template_name = "category_list.html"
    paginate_by = 5

    def get_queryset(self):

        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                name__icontains=query
            )

        return qs

    def get_ordering(self):

        allowed = [
            "name",
            "created_at",
        ]

        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "name"


class CategoryCreateView(CreateView):

    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryUpdateView(UpdateView):

    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(DeleteView):

    model = Category
    template_name = "category_delete.html"
    success_url = reverse_lazy("category-list")


class PriorityList(ListView):

    model = Priority
    context_object_name = "priorities"
    template_name = "priority_list.html"
    paginate_by = 5

    def get_queryset(self):

        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                name__icontains=query
            )

        return qs

    def get_ordering(self):

        allowed = [
            "name",
            "created_at",
        ]

        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "name"


class PriorityCreateView(CreateView):

    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority-list")


class PriorityUpdateView(UpdateView):

    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority-list")


class PriorityDeleteView(DeleteView):

    model = Priority
    template_name = "priority_delete.html"
    success_url = reverse_lazy("priority-list")


class NoteList(ListView):

    model = Note
    context_object_name = "notes"
    template_name = "note_list.html"
    paginate_by = 5

    def get_queryset(self):

        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:

            qs = qs.filter(
                Q(content__icontains=query)
                | Q(task__title__icontains=query)
            )

        return qs

    def get_ordering(self):

        allowed = [
            "created_at",
            "task__title",
        ]

        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "-created_at"


class NoteCreateView(CreateView):

    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note-list")


class NoteUpdateView(UpdateView):

    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note-list")


class NoteDeleteView(DeleteView):

    model = Note
    template_name = "note_delete.html"
    success_url = reverse_lazy("note-list")


class SubTaskList(ListView):

    model = SubTask
    context_object_name = "subtasks"
    template_name = "subtask_list.html"
    paginate_by = 5

    def get_queryset(self):

        qs = super().get_queryset()

        query = self.request.GET.get("q")

        if query:

            qs = qs.filter(
                Q(title__icontains=query)
                | Q(status__icontains=query)
                | Q(parent_task__title__icontains=query)
            )

        return qs

    def get_ordering(self):

        allowed = [
            "title",
            "status",
            "parent_task__title",
            "created_at",
        ]

        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return sort_by

        return "title"


class SubTaskCreateView(CreateView):

    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask-list")


class SubTaskUpdateView(UpdateView):

    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask-list")


class SubTaskDeleteView(DeleteView):

    model = SubTask
    template_name = "subtask_delete.html"
    success_url = reverse_lazy("subtask-list")