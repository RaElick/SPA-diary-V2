from .models import Task
from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields = ["title", "task", "date"]
        exclude = ["author"]
        widgets = {
            "author": TextInput(attrs={
            }),
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

