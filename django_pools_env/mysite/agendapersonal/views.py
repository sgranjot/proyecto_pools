from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from .models import Event, Task


class IndexView(generic.ListView):
    template_name = 'agendapersonal/index.html'
    context_object_name = 'events_tasks_list'

    def get_queryset(self):
        """Return the events and tasks that have not finished yet"""
        queryset_events = Event.objects.filter(end_time__gte=timezone.now()).order_by('-start_time')
        queryset_tasks = Task.objects.filter(status=False)
        events_tasks_list = list(queryset_events) + list(queryset_tasks)
        return events_tasks_list
        # __gte significa mayor o igual que (greater than or equal to)


class DetailView(generic.DetailView):
    model = Event
    template_name = 'agendapersonal/detail.html'

    def get_queryset(self):
        return Event.objects.all()

