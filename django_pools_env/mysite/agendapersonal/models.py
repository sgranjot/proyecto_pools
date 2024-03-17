from django.db import models


class Event(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=200)
    completion_date = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return self.title


