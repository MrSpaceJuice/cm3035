from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class ProfileForm(forms.ModelForm): 
    class Meta:
        model = Profile
        fields = ('status',)
        labels = {'status': '',}

class UserStatusForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('status',)

class NewCourseForm(forms.ModelForm):
    teacher = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta:
        model = Course
        fields = ('course', 'name')

class EnrollForm(forms.ModelForm):
    class Meta:
        model = CourseUserLink
        fields = ('user', 'course',)

class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model = CourseMaterials
        fields = ('material',)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = CourseUserLink
        fields = ('feedback',)

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)