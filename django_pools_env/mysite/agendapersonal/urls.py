from django.urls import path

from . import views

app_name = 'agendapersonal'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),                          # ex: /agendapersonal/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),               # ex: /agendapersonal/5/
]
