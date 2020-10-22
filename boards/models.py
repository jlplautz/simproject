from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    # __str__ method is a String representation of an object.
    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    # parameter auto_now_add= True -> inform Django to set de current date and time
    last_updated = models.DateTimeField(auto_now_add=True)
    # parameter related_name -> will be used to create a reverse relationship where Board will
    # access a list of topic instances that belong to it
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    # related_name='+' -> this instructs Django that we don need this reverse relationship.
    # so it is ignore
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
