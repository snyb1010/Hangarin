from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from studentorg.models import Category, Note, Priority, SubTask, Task


class Command(BaseCommand):
    help = "Populate Hangarin data: priorities, categories, tasks, notes, and subtasks"

    def add_arguments(self, parser):
        parser.add_argument("--tasks", type=int, default=25)
        parser.add_argument("--notes", type=int, default=2)
        parser.add_argument("--subtasks", type=int, default=3)
        parser.add_argument(
            "--keep-existing",
            action="store_true",
            help="Do not clear existing records before seeding",
        )

    def handle(self, *args, **options):
        fake = Faker()
        task_count = options["tasks"]
        notes_per_task = options["notes"]
        subtasks_per_task = options["subtasks"]
        keep_existing = options["keep_existing"]

        priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        categories = ["Work", "School", "Personal", "Finance", "Projects"]
        statuses = ["Pending", "In Progress", "Completed"]

        # Default behavior: clear old content first for clean, expected output.
        if not keep_existing:
            Note.objects.all().delete()
            SubTask.objects.all().delete()
            Task.objects.all().delete()
            Priority.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.WARNING("Existing Task/Note/SubTask/Priority/Category data cleared."))

        for name in priorities:
            Priority.objects.get_or_create(name=name)

        for name in categories:
            Category.objects.get_or_create(name=name)

        priority_qs = list(Priority.objects.all())
        category_qs = list(Category.objects.all())

        created_tasks = 0
        created_notes = 0
        created_subtasks = 0

        for _ in range(task_count):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=statuses),
                priority=fake.random_element(elements=priority_qs),
                category=fake.random_element(elements=category_qs),
            )
            created_tasks += 1

            for _ in range(notes_per_task):
                Note.objects.create(task=task, content=fake.paragraph(nb_sentences=2))
                created_notes += 1

            for _ in range(subtasks_per_task):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=5),
                    status=fake.random_element(elements=statuses),
                )
                created_subtasks += 1

        self.stdout.write(self.style.SUCCESS(f"Created tasks: {created_tasks}"))
        self.stdout.write(self.style.SUCCESS(f"Created notes: {created_notes}"))
        self.stdout.write(self.style.SUCCESS(f"Created subtasks: {created_subtasks}"))
