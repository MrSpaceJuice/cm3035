from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework import mixins

class CourseDetails(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class UserDetails(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileDetails(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TeacherDetails(generics.ListCreateAPIView):
    queryset = Profile.objects.filter(teacher=True).all()
    serializer_class = ProfileSerializer

