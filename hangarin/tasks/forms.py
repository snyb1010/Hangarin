from django import forms
from .models import Note, SubTask, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "deadline", "priority", "category"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        deadline_value = self.initial.get("deadline") or getattr(self.instance, "deadline", None)
        if deadline_value:
            self.initial["deadline"] = deadline_value.strftime("%Y-%m-%dT%H:%M")


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ["title", "status"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["content"]
