from django import forms
from .models import Projects,Lessons,SubLessons,VideoLessons,Completed,DelURLS

class ProjectForms(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['name']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['name']

class SubLessonForum(forms.ModelForm):
    class Meta:
        model = SubLessons
        fields = ['name']


class VideoLessonsForum(forms.ModelForm):
    class Meta:
        model = VideoLessons
        fields = ['url','chanel','isVideo','isImage','isWeb','countValue']


class DeleteUrlForum(forms.ModelForm):
    class Meta:
        model = VideoLessons
        fields = ['url']


class CompletedForum(forms.ModelForm):
    class Meta:
        model = Completed
        fields = ['isChecked']

class DelForum(forms.ModelForm):
    class Meta:
        model = DelURLS
        fields = ['url']
