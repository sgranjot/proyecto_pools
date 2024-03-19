from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse, reverse_lazy

from .forms import EventForm, TaskForm

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
    form_class = EventForm
    template_name = 'agendapersonal/createEvent.html'
    success_url = reverse_lazy('agendapersonal:indexEvent')


class CreateTaskView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'agendapersonal/createTask.html'
    success_url = reverse_lazy('agendapersonal:indexTask')

