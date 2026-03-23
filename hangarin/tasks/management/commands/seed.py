from django.core.management.base import BaseCommand
from faker import Faker
from tasks.models import Task, SubTask, Note, Category, Priority
from django.utils import timezone
import random

fake = Faker()

class Command(BaseCommand):
    help = "Seed Priority, Category, Task, SubTask, and Note data."

    def handle(self, *args, **kwargs):
        required_priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        required_categories = ["Work", "School", "Personal", "Finance", "Projects"]

        for name in required_priorities:
            Priority.objects.get_or_create(name=name)

        for name in required_categories:
            Category.objects.get_or_create(name=name)

        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        if not categories or not priorities:
            self.stdout.write(self.style.ERROR("Missing categories or priorities. Seeding aborted."))
            return

        for _ in range(20):
            deadline = fake.date_time_this_month()
            if timezone.is_naive(deadline):
                deadline = timezone.make_aware(deadline)

            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                deadline=deadline,
                priority=random.choice(priorities),
                category=random.choice(categories),
            )

            for _ in range(3):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=3),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                    task=task
                )

            for _ in range(2):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph()
                )

        self.stdout.write(self.style.SUCCESS("Seeding complete."))
