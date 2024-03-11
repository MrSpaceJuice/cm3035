from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.courses, name='courses'),
    path('courses/create/', views.new_course, name='new-course'),
    path('courses/<int:pk>', views.course_details, name='course-details'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('user/<int:pk>', views.user, name='user'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('enroll/', views.enroll, name='enroll'), 
    path('feedback/', views.feedback, name='feedback'),
    
    path('api/course/<int:pk>', api.CourseDetails.as_view()),
    path('api/users', api.UserDetails.as_view()),
    path('api/user-profile/', api.ProfileDetails.as_view()),
    path('api/teachers', api.TeacherDetails.as_view()),

    path('chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
]