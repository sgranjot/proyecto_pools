from django import forms
from .models import Event, Task


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class UpdateEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateEventForm, self).__init__(*args, **kwargs)
        # Establecer el valor inicial de fechaInicio
        self.fields['start_time'].widget.attrs['value'] = self.instance.start_time.strftime('%Y-%m-%dT%H:%M')
        # Establecer el valor inicial de fechaFin
        self.fields['end_time'].widget.attrs['value'] = self.instance.end_time.strftime('%Y-%m-%dT%H:%M')


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completion_date', 'status']
        widgets = {
            'completion_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.CheckboxInput(attrs={'label': 'Completada'}),
        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completion_date', 'status']
        widgets = {
            'completion_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.CheckboxInput(attrs={'label': 'Completada'}),
        }

    def __init__(self, *args, **kwargs):
        super(UpdateTaskForm, self).__init__(*args, **kwargs)
        # Establecer el valor inicial de fecha
        self.fields['completion_date'].widget.attrs['value'] = self.instance.completion_date.strftime('%Y-%m-%dT%H:%M')

