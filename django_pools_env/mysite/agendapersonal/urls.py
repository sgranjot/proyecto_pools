from django.urls import path

from . import views

app_name = 'agendapersonal'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),                                # ex: /agendapersonal/
    path('indexEvent/', views.IndexEventView.as_view(), name='indexEvent'),           # ex: /agendapersonal/indexEvent/
    path('indexTask/', views.IndexTaskView.as_view(), name='indexTask'),              # ex: /agendapersonal/indexTask/
    path('<int:pk>/event/', views.DetailEventView.as_view(), name='eventDetail'),     # ex: /agendapersonal/2/event/
    path('<int:pk>/task/', views.DetailTaskView.as_view(), name='taskDetail'),        # ex: /agendapersonal/2/task/
    path('createEvent/', views.CreateEventView.as_view(), name='createEvent'),        # ex. /agendapersonal/createEvent/
    path('createTask/', views.CreateTaskView.as_view(), name='createTask'),           # ex. /agendapersonal/createTask/
]
