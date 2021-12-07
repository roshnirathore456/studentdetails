from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('teacherclick', views.teacherclick_view),
    path('studentclick', views.studentclick_view),
    path('teachersignup', views.teacher_signup_view,name='teachersignup'),
    path('teacherlogin', views.teacher_login_view,name='teacherlogin'),
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('studentlogin', views.student_login_view,name='studentlogin'),
    path('home', views.home, name='home'),
    path('studentdetails', views.studentdetails_view,name='studentdetails'),
    path('teacherfetch', views.teacher_fetch_student_details,name='teacherfetch'),
]
