# Hangarin

## Hangarin: Task & To-Do Manager

The Hangarin is a simple web application built with Django,
that helps users organize their daily tasks, manage priorities,
add notes, and break down large goals into smaller subtasks.

Figure 1 Entity Relationship Diagram

Given the ERD above create the application with following requirements:
- Prepare virtual environment for this project.
- Use version control in managing your code.
- Deploy the project in PythonAnywhere.

## 1. Model

- Inherit BaseModel with created_at and updated_at fields.
- Add __str__ method for each model.
- Use field choices (enumeration) in status fields.
  This will generate dropdown in Admin side.

```python
status = models.CharField(
    max_length=50,
    choices=[
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ],
    default="Pending"
)
```

## 2. Populating Data

- Manually add record to Priority (high, medium, low, critical, and optional)
  and Category (Work, School, Personal, Finance, Projects).
- Use faker package in generating fake data for Task, Notes, and SubTask models.
  - For task title use sentence()
  - For task description use paragraph()
  - For status use random_element()

```python
fake.sentence(nb_words=5)
# -> Generates a random sentence consisting of about nb_words words.
#    It starts with a capital letter and ends with a period (.).

fake.paragraph(nb_sentences=3)
# -> Generates a random paragraph with about nb_sentences sentences.

fake.random_element(elements=["Pending", "In Progress", "Completed"])
# -> Returns a random value from the given sequence (list, tuple, set, or dict).

from django.utils import timezone
deadline = timezone.make_aware(fake.date_time_this_month())

# fake.date_time_this_month() -> Generates a random datetime object within the current month.
# timezone.make_aware() -> Takes a naive datetime and converts it into
#                           a timezone-aware datetime (project configured timezone).
```

## 3. Admin

TaskAdmin:
- Display title, status, deadline, priority, category.
- Add filters for status, priority, category.
- Enable search on title and description.

SubTaskAdmin:
- Display title, status, and a custom field parent_task_name.
- Filter by status.
- Enable search on title.

CategoryAdmin and PriorityAdmin:
- Display just the name field.
- Make them searchable.

NoteAdmin:
- Display task, content, and created_at.
- Filter by created_at.
- Enable search on content.

## 4. Refactor

- To replace the "Categorys" and "Prioritys" which are not grammatically correct,
  add verbose_name_plural attribute.

```python
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
```

## Run Locally

```bash
psusenv\Scripts\activate
pip install -r requirements.txt
cd projectsite
python manage.py makemigrations
python manage.py migrate
python manage.py seed_hangarin_data --tasks 25
# Use --keep-existing if you do NOT want to clear old data first
# python manage.py seed_hangarin_data --tasks 25 --keep-existing
python manage.py runserver
```
