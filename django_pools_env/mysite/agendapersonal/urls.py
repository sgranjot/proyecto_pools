from django.urls import path

from . import views

app_name = 'agendapersonal'
urlpatterns = [
    path('', views.index, name='index'),                           # ex: /agendapersonal/
]
