from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from faker import Faker

from hangarin.models import Category, Priority, Task, Note, SubTask


class Command(BaseCommand):

    help = "Create initial fake data for Tasks, Notes, and SubTasks"

    def handle(self, *args, **kwargs):

        self.create_users(3)
        self.create_tasks(40)
        self.create_notes(35)
        self.create_subtasks(50)

    def create_users(self, count):

        fake = Faker()

        for _ in range(count):

            username = fake.unique.user_name()

            User.objects.create_user(
                username=username,
                email=fake.unique.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )

        self.stdout.write(
            self.style.SUCCESS("Users created successfully.")
        )

    def create_tasks(self, count):

        fake = Faker()

        users = list(User.objects.all())
        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        if not users:
            self.stdout.write(
                self.style.ERROR(
                    "No users found. Users must be created first."
                )
            )
            return

        if not categories:
            self.stdout.write(
                self.style.ERROR(
                    "No categories found. Create categories first."
                )
            )
            return

        if not priorities:
            self.stdout.write(
                self.style.ERROR(
                    "No priorities found. Create priorities first."
                )
            )
            return

        for _ in range(count):

            Task.objects.create(

                user=fake.random_element(
                    elements=users
                ),

                title=fake.sentence(
                    nb_words=5
                ),

                description=fake.paragraph(
                    nb_sentences=3
                ),

                deadline=fake.date_between(
                    start_date="today",
                    end_date="+30d"
                ),

                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed"
                    ]
                ),

                category=fake.random_element(
                    elements=categories
                ),

                priority=fake.random_element(
                    elements=priorities
                ),
            )

        self.stdout.write(
            self.style.SUCCESS("Tasks created successfully.")
        )

    def create_notes(self, count):

        fake = Faker()

        tasks = list(Task.objects.all())

        if not tasks:
            self.stdout.write(
                self.style.ERROR(
                    "No tasks found. Create tasks first."
                )
            )
            return

        for _ in range(count):

            Note.objects.create(

                task=fake.random_element(
                    elements=tasks
                ),

                content=fake.paragraph(
                    nb_sentences=2
                ),
            )

        self.stdout.write(
            self.style.SUCCESS("Notes created successfully.")
        )

    def create_subtasks(self, count):

        fake = Faker()

        tasks = list(Task.objects.all())

        if not tasks:
            self.stdout.write(
                self.style.ERROR(
                    "No tasks found. Create tasks first."
                )
            )
            return

        for _ in range(count):

            SubTask.objects.create(

                parent_task=fake.random_element(
                    elements=tasks
                ),

                title=fake.sentence(
                    nb_words=4
                ),

                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed"
                    ]
                ),
            )

        self.stdout.write(
            self.style.SUCCESS("SubTasks created successfully.")
        )