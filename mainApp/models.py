from django.db import models
from django.utils import timezone

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=128,unique=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Lessons(models.Model):
    project_name = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_name


class SubLessons(models.Model):
    project_name = models.CharField(max_length=128)
    lesson_name = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    date = models.DateTimeField(default=timezone.now)
    webUpdate = models.BooleanField(default=True)
    mobUpdate = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name 


class VideoLessons(models.Model):
    project_name = models.CharField(max_length=128)
    lesson_name = models.CharField(max_length=128)
    sublesson_name = models.CharField(max_length=256)
    url = models.CharField(max_length=1024,unique=True)
    emb_url = models.CharField(max_length=1024,default='')
    chanel = models.CharField(max_length=128,default='unknown')
    description = models.TextField(null=True)
    isVideo = models.BooleanField(default=True)
    isImage = models.BooleanField(default=False)
    isWeb = models.BooleanField(default=False)
    countValue = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['countValue']

    def __str__(self):
        return self.project_name 

class Completed(models.Model):
    project_name = models.CharField(max_length=128)
    lesson_name = models.CharField(max_length=128)
    sublesson_name = models.CharField(max_length=256)
    date = models.DateTimeField(default=timezone.now)
    isChecked = models.BooleanField(default=False)
    def __str__(self):
        return self.project_name

class DelURLS(models.Model):
    url = models.TextField()

    def __str__(self):
        return self.url