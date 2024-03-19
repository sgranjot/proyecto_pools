from django import forms
from .models import Event, Task


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'date'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'date'}),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completion_date', 'status']
        widgets = {
            'completion_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'status': forms.CheckboxInput(attrs={'label': 'Completada'}),
        }
