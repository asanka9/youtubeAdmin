from django.contrib import admin
from .models import  Projects,Lessons,SubLessons,VideoLessons,Completed

# Register your models here.
admin.site.register(Projects)
admin.site.register(Lessons)
admin.site.register(SubLessons)
admin.site.register(VideoLessons)
admin.site.register(Completed)
