from django.forms import ModelForm
from django import forms
from datetime import datetime, time as dt_time
from django.utils import timezone
from .models import Task, SubTask, Note, Category, Priority


class StyledModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            widget = field.widget
            css_class = "form-control"
            if isinstance(widget, forms.CheckboxInput):
                css_class = "form-check-input"
            elif isinstance(widget, forms.SelectMultiple):
                css_class = "form-control"
            widget.attrs["class"] = f"{widget.attrs.get('class', '')} {css_class}".strip()
            if isinstance(widget, forms.Textarea):
                widget.attrs.setdefault("rows", 4)
            if not isinstance(widget, forms.CheckboxInput):
                widget.attrs.setdefault("placeholder", field.label)


class TaskForm(StyledModelForm):
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=["%Y-%m-%d"],
    )

    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        deadline_value = self.initial.get("deadline") or getattr(self.instance, "deadline", None)
        if deadline_value:
            self.initial["deadline"] = deadline_value.date()

    def clean_deadline(self):
        selected_date = self.cleaned_data["deadline"]
        deadline_dt = datetime.combine(selected_date, dt_time.min)
        if timezone.is_naive(deadline_dt) and timezone.is_aware(timezone.now()):
            deadline_dt = timezone.make_aware(deadline_dt, timezone.get_current_timezone())
        return deadline_dt


class SubTaskForm(StyledModelForm):
    class Meta:
        model = SubTask
        fields = "__all__"


class NoteForm(StyledModelForm):
    class Meta:
        model = Note
        fields = "__all__"


class CategoryForm(StyledModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class PriorityForm(StyledModelForm):
    class Meta:
        model = Priority
        fields = "__all__"
