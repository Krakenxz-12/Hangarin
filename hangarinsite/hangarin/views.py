from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
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

from .forms import (
    TaskForm,
    CategoryForm,
    PriorityForm,
    NoteForm,
    SubTaskForm,
    RegisterForm,
    ProfileForm,
)

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

class UserLoginView(LoginView):
    template_name = "login.html"

class UserLogoutView(LogoutView):
    next_page = "/login/"

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "register.html"
    success_url = "/"
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object, backend="django.contrib.auth.backends.ModelBackend")
        return response

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "profile_edit.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

class SettingsView(LoginRequiredMixin, TemplateView):
    template_name = "settings.html"

class HomePageView(LoginRequiredMixin, ListView):

    model = Task
    template_name = "home.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        user_tasks = Task.objects.filter(user=self.request.user)

        context["total_tasks"] = user_tasks.count()
        context["total_categories"] = Category.objects.count()
        context["total_priorities"] = Priority.objects.count()
        context["total_notes"] = Note.objects.count()
        context["total_subtasks"] = SubTask.objects.count()
        context["completed_tasks"] = user_tasks.filter(status="Completed").count()
        context["pending_tasks"] = user_tasks.filter(status="Pending").count()
        context["in_progress_tasks"] = user_tasks.filter(status="In Progress").count()

        return context
    
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "task"
    template_name = "task_list.html"
    paginate_by = 5

    def get_queryset(self):
        qs = Task.objects.filter(
            user=self.request.user
        )

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


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
        )

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_del.html"
    success_url = reverse_lazy("task-list")

    def get_queryset(self):
        return Task.objects.filter(
            user=self.request.user
        )

class CategoryList(LoginRequiredMixin, ListView):
    
    model = Category
    context_object_name = "categories"
    template_name = "categories_list.html"
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


class CategoryCreateView(LoginRequiredMixin, CreateView):

    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryUpdateView(LoginRequiredMixin, UpdateView):

    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(LoginRequiredMixin, DeleteView):

    model = Category
    template_name = "category_del.html"
    success_url = reverse_lazy("category-list")


class PriorityList(LoginRequiredMixin, ListView):

    model = Priority
    context_object_name = "priorities"
    template_name = "prio_list.html"
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


class PriorityCreateView(LoginRequiredMixin, CreateView):

    model = Priority
    form_class = PriorityForm
    template_name = "prio_form.html"
    success_url = reverse_lazy("prio-list")


class PriorityUpdateView(LoginRequiredMixin, UpdateView):

    model = Priority
    form_class = PriorityForm
    template_name = "prio_form.html"
    success_url = reverse_lazy("prio-list")


class PriorityDeleteView(LoginRequiredMixin, DeleteView):

    model = Priority
    template_name = "prio_del.html"
    success_url = reverse_lazy("prio-list")


class NoteList(LoginRequiredMixin, ListView):

    model = Note
    context_object_name = "notes"
    template_name = "notes_list.html"
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


class NoteCreateView(LoginRequiredMixin, CreateView):

    model = Note
    form_class = NoteForm
    template_name = "notes_form.html"
    success_url = reverse_lazy("note-list")


class NoteUpdateView(LoginRequiredMixin, UpdateView):

    model = Note
    form_class = NoteForm
    template_name = "notes_form.html"
    success_url = reverse_lazy("note-list")


class NoteDeleteView(LoginRequiredMixin, DeleteView):

    model = Note
    template_name = "note_del.html"
    success_url = reverse_lazy("note-list")


class SubTaskList(LoginRequiredMixin, ListView):

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


class SubTaskCreateView(LoginRequiredMixin, CreateView):

    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask-list")


class SubTaskUpdateView(LoginRequiredMixin, UpdateView):

    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask-list")


class SubTaskDeleteView(LoginRequiredMixin, DeleteView):

    model = SubTask
    template_name = "subtask_del.html"
    success_url = reverse_lazy("subtask-list")