from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('home/',views.projects,name='mainApp-home'),
    path('home/<pname>',views.lessons,name='mainApp-lessons'),
    path('home/<pname>/<lname>',views.sub_lessons,name='mainApp-sub_lessons'),
    path('home/<pname>/<lname>/<sname>',views.video_lessons,name='mainApp-video_lessons'),
    path('home/completed/',views.checking,name='com'),
    path('home/deletec/<pname>/<lname>/<sname>',views.deleteURLS,name='del'),
    path('home/deletec/<pname>/<lname>/<sname>/<url>',views.deleteURLS01,name='del1'),
    path('delete/deleteAll',views.deleteAll,name='delAll')

]