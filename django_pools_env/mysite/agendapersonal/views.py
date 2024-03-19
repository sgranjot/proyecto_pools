from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse

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


class CreateEventView(generic.CreateView):
    model = Event

