from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Projects,Lessons,SubLessons,VideoLessons,Completed
from .forms import ProjectForms,LessonForm,SubLessonForum,VideoLessonsForum,DeleteUrlForum,CompletedForum,DelForum
from django.contrib import messages

project_name = ''
lesson_name = ''
sublesson_name = ''

#Commented 2020

@login_required
def home(request):
    return redirect('mainApp-home')

@login_required
def projects(request):
    if request.method == 'POST':
        p_form = ProjectForms(request.POST)
        if p_form.is_valid():
            p_form.save()
            messages.success(request,f'Project added Succesful !')
            return redirect('mainApp-home')
    else:
        p_form = ProjectForms()

    context = {
        'projects': Projects.objects.all(),
        'form':p_form
    }
    return render(request,'mainApp/projects.html',context)

@login_required
def lessons(request,pname):
    if request.method == 'POST':
        p_form = LessonForm(request.POST)
        if p_form.is_valid():
            name = p_form.cleaned_data.get('name')
            lesson = Lessons()
            lesson.name = name
            lesson.project_name = pname
            messages.success(request,f'Lesson added Succesful !')
            lesson.save()
            
    else:
        p_form = ProjectForms()
    context = {
        'lessons': Lessons.objects.filter(project_name = pname),
        'project':pname,
        'form':p_form

    }
    return render(request,'mainApp/lessons.html',context)

@login_required
def sub_lessons(request,pname,lname):
    if request.method == 'POST':
        p_form = SubLessonForum(request.POST)
        if p_form.is_valid():
            name = p_form.cleaned_data.get('name')
            lesson = SubLessons()
            lesson.name = name
            lesson.project_name = pname
            lesson.lesson_name = lname
            lesson.save()
            messages.success(request,f'Sub Lesson added Succesful !')

            
    else:
        p_form = ProjectForms()
    context = {
        'sublessons': SubLessons.objects.filter(project_name = pname,lesson_name=lname),
        'project':pname,
        'lesson':lname,
        'form':p_form
    }
    return render(request,'mainApp/sub_lessons.html',context)


@login_required
def video_lessons(request,pname,lname,sname):
    if request.method == 'POST':
        p_form = VideoLessonsForum(request.POST)
        # ['url','chanel','isVideo']

        if p_form.is_valid():
            url = p_form.cleaned_data.get('url')
            chanel = p_form.cleaned_data.get('chanel')
            isVideo = p_form.cleaned_data.get('isVideo')
            isImage = p_form.cleaned_data.get('isImage')
            countValue = p_form.cleaned_data.get('countValue')
            isWeb = p_form.cleaned_data.get('isWeb')
            description = p_form.cleaned_data.get('description')
            lesson = VideoLessons()
            lesson.url = url
            if isVideo:
                lesson.emb_url = url.replace('watch?v=','embed/')
            lesson.chanel = chanel
            lesson.isVideo = isVideo
            lesson.isImage = isImage
            lesson.isWeb = isWeb
            lesson.description = description
            lesson.project_name = pname
            lesson.lesson_name = lname
            lesson.sublesson_name = sname
            try:
                Completed.objects.filter(project_name = pname,lesson_name=lname,sublesson_name=sname)[0]
            except:
                completed = Completed()
                completed.project_name = pname
                completed.lesson_name = lname
                completed.sublesson_name = sname
                completed.save()
            lesson.save()
            messages.success(request,f'Sub Lesson added Succesful !')
    else:
        p_form = VideoLessonsForum()


    context = {
        'vlessons01': VideoLessons.objects.filter(project_name=pname,lesson_name=lname,sublesson_name=sname),
        'form':p_form,
        'pname':pname,
        'lname':lname,
        'sname':sname 
        

    }
    return render(request,'mainApp/video_lessons.html',context)


@login_required
def checking(request):
    if request.method == 'POST':
        form = CompletedForum(request.POST)
        if form.is_valid():
            pass
    else:
        form = CompletedForum()
    context = {
        'coms' : Completed.objects.all(),
        'form' : form
    }
    return render(request,'mainApp/completed.html',context)

@login_required
def deleteURLS(request,pname,lname,sname):
    cm = Completed.objects.filter(project_name = pname,lesson_name=lname,sublesson_name=sname)
    cm.delete()
    return redirect('com')

@login_required
def deleteURLS01(request,pname,lname,sname,url):

    cm = VideoLessons.objects.filter(id = url)
    try:
        Completed.objects.filter(project_name = pname,lesson_name=lname,sublesson_name=sname)[0]
    except:
        completed = Completed()
        completed.project_name = pname
        completed.lesson_name = lname
        completed.sublesson_name = sname
        completed.save()
    cm.delete()
    return video_lessons(request,pname,lname,sname)


@login_required
def deleteAll(request):
    if request.method == 'POST':
        p_form = DelForum(request.POST)
        if p_form.is_valid():
            url = p_form.cleaned_data.get('url')
            temp_list = url.split(',')
            for url in temp_list:
                obj = VideoLessons.objects.filter(url=url)
                obj.delete()
            messages.success(request,f'Record Deleted Succesful !')
    else:
        p_form = DelForum()
    context = {
        'form':p_form
    }
    return render(request,'mainApp/deleteAllURL.html',context)
