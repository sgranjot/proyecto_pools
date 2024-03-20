from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse, reverse_lazy

from .forms import CreateEventForm, UpdateEventForm, CreateTaskForm, UpdateTaskForm

from .models import Event, Task


class IndexView(generic.TemplateView):
    template_name = 'agendapersonal/index.html'


class IndexEventView(generic.ListView):
    template_name = 'agendapersonal/indexEvent.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        """Return events that have not finished yet"""
        return Event.objects.filter(end_time__gte=timezone.now()).order_by('-start_time')
        # __gte significa mayor o igual que (greater than or equal to)


class IndexTaskView(generic.ListView):
    template_name = 'agendapersonal/indexTask.html'
    context_object_name = 'tasks_list'

    def get_queryset(self):
        """Return tasks that have not finished yet"""
        return Task.objects.filter(status=False)


class DetailEventView(generic.DetailView):
    model = Event
    template_name = 'agendapersonal/eventDetail.html'
    context_object_name = 'object'


class DetailTaskView(generic.DetailView):
    model = Task
    template_name = 'agendapersonal/taskDetail.html'
    context_object_name = 'object'


class CreateEventView(generic.CreateView):
    model = Event
    form_class = CreateEventForm                                      #si no personalizamos el formulario pondriamos: fields = ['title', 'description', 'fechaInicio', 'fechaFin']
    template_name = 'agendapersonal/createEvent.html'
    success_url = reverse_lazy('agendapersonal:indexEvent')


class CreateTaskView(generic.CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = 'agendapersonal/createTask.html'
    success_url = reverse_lazy('agendapersonal:indexTask')


class UpdateEventView(generic.UpdateView):
    model = Event
    form_class = UpdateEventForm
    template_name = 'agendapersonal/updateEvent.html'
    success_url = reverse_lazy('agendapersonal:indexEvent')


class UpdateTaskView(generic.UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = 'agendapersonal/updateTask.html'
    success_url = reverse_lazy('agendapersonal:indexTask')


class DeleteEventView(generic.DeleteView):
    model = Event
    template_name = 'agendapersonal/deleteEvent.html'
    success_url = reverse_lazy('agendapersonal:indexEvent')


class DeleteTaskView(generic.DeleteView):
    model = Task
    template_name = 'agendapersonal/deleteTask.html'
    success_url = reverse_lazy('agendapersonal:indexTask')



