from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields = ["title", "task", "date"]
        widgets = {
            "title" : TextInput(attrs={
                'class':'title-form-control',
                'placeholder':'Введите название'
            }),
            "task": Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Введите описание'
            }),
            "date": DateTimeInput(attrs={
                'class': 'datetime-input',
                'placeholder': 'Дата заметки'
            })
        }

