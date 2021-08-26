from django.db import models
from django.db.models.deletion import PROTECT
from core.models import Client

# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class ProjectType(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=200, null=False)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    project_type = models.ForeignKey(ProjectType, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class UserStory(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=1000, null=False)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    uploaded_file = models.FileField(upload_to="User-Story-Files/", default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    title = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=1000, null=False)
    user_story = models.ForeignKey(UserStory, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    uploaded_file = models.FileField(upload_to="Task-Files/", default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Comment(models.Model):
    description = models.CharField(max_length=500, null=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description