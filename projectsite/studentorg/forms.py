from django.forms import ModelForm
from django import forms
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
    class Meta:
        model = Task
        fields = "__all__"


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
