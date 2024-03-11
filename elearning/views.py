from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from .models import *
from .forms import *

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def courses(request):
    teacher_courses = Course.objects.filter(teacher = request.user.id)
    courses = Course.objects.exclude(student = request.user.id).all()
    return render(request, 'courses.html', {'courses': courses, 
                                            'teacher_courses': teacher_courses})

def course_details(request, pk):
    course = Course.objects.get(pk=pk)
    students = course.student.all()
    materials = CourseMaterials.objects.filter(course=course)

    if request.method == 'POST':
        print(request.POST)
        new_form = CourseMaterialForm(request.POST, request.FILES)
        if new_form.is_valid():
            new_form = new_form.save(commit=False)
            new_form.user = request.user
            new_form.course = course
            new_form.save()
        return HttpResponseRedirect('/courses/'+str(course.id))
    else:
        form = CourseMaterialForm()
    
    return render(request, 'course-details.html', {'course': course, 
                                                   'students': students,
                                                   'materials': materials,
                                                   'form': form})

def new_course(request):
    if request.method == 'POST':
        course_form = NewCourseForm(request.POST)
        
        if course_form.is_valid() :
            course_form = course_form.save(commit=False)
            course_form.teacher = request.user
            course_form.save()
        return HttpResponseRedirect('/courses')
    
    else:
        course_form = NewCourseForm()

    return render(request, 'new-course.html', {'course_form': course_form})

# Only returns a user if they are not staff (admin) and not a teacher
def students(request):
    students = User.objects.filter(Q(is_staff=False) & Q(profile__teacher=False)).all()
    return render(request, 'students.html', {'students': students})

# Only returns a user if they are not staff (admin) and they are a teacher
def teachers(request):
    teachers = User.objects.filter(Q(is_staff=False) & Q(profile__teacher=True)).all()
    return render(request, 'teachers.html', {'teachers': teachers})

def user(request, pk):
    users = User.objects.get(pk=pk)
    user_profile = Profile.objects.get(user = users)
    # Uses the through table to select the courses that 
    # a user is enrolled in based on user id.
    courses = CourseUserLink.objects.filter(user = users.id).select_related()
    deadline_array = []

    # loops through the courses and gets the deadlines
    for i in range(0, len(courses)):
        current_pk = courses[i].course
        deadlines = Deadline.objects.filter(course = current_pk)
        for j in range(0,len(deadlines)):
            deadline_array.append(deadlines[j])

    # handles the post request for status updates
    if request.method == 'POST':
        status_form = ProfileForm(request.POST)
        if status_form.is_valid():
            user_profile.status = status_form.cleaned_data['status']
            user_profile.save()
            return HttpResponseRedirect('/user/'+str(users.id))
    else: 
        # provides a form for user to update their status
        status_form = UserStatusForm(initial={'status': user_profile.status})
        feedback_form = FeedbackForm()
        return render(request, 'user.html', {'users': users, 
                                            'user_profile': user_profile, 
                                            'status_form': status_form,
                                            'feedback_form': feedback_form,
                                            'courses': courses,
                                            'deadlines': deadline_array
                                            })

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        user_form = UserForm()

    return render(request, 'register.html', {'user_form': user_form, 
                                          'registered': registered})
 
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else: 
                return HttpResponse('Your account is disabled')

        else:
            return HttpResponse('Invalid Login')
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def enroll(request):
    if request.method == 'POST':
        new_course = EnrollForm(request.POST)
        print(new_course)
        if new_course.is_valid() :
            new_course.save()
            return HttpResponseRedirect('/courses')

def feedback(request):
    course_id = request.POST['course'] 
    user_id = request.POST['user']
    user_course = CourseUserLink.objects.filter(course = course_id, user = user_id)
    entry = user_course[0]
    entry.feedback = request.POST['feedback']
    entry.save()
    return HttpResponseRedirect('/students')

def chat(request):
    return render(request, 'chat.html')

def room(request, room_name):
    return render(request, 'room.html', {'room_name': room_name})

########################################################################################
def test(request):
    if request.user.profile.teacher:
        test = "Worked"
    else:
        test = "Failed"

    print(request.user.profile.picture.url)

    return render(request, 'test.html', {'test': test})