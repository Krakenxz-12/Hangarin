from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from hangarin.models import Task, Note, SubTask, Priority, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        fake = Faker()

        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        for i in range(10):

            task = Task.objects.create(
                title=fake.sentence(nb_words=5),

                description=fake.paragraph(
                    nb_sentences=3
                ),

                status=fake.random_element(
                    elements=[
                        "Pending",
                        "In Progress",
                        "Completed"
                    ]
                ),

                deadline=timezone.make_aware(
                    fake.date_time_this_month()
                ),

                priority=random.choice(priorities),

                category=random.choice(categories)
            )

            for j in range(2):

                Note.objects.create(
                    task=task,
                    content=fake.paragraph(
                        nb_sentences=2
                    )
                )

            for j in range(3):

                SubTask.objects.create(
                    title=fake.sentence(
                        nb_words=5
                    ),

                    status=fake.random_element(
                        elements=[
                            "Pending",
                            "In Progress",
                            "Completed"
                        ]
                    ),

                    parent_task=task
                )

        self.stdout.write(
            self.style.SUCCESS(
                "Fake data successfully created!"
            )
        )