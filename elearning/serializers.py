from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)

        # fields = ['first_name','last_name']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = TeacherSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    student = ProfileSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = '__all__'

class CourseUserLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseUserLink
        fields = '__all__'
        lookup_field = "user"




