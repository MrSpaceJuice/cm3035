import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File

from .models import *

class ProfileFactory(factory.django.DjangoModelFactory):
    user = "TestUser"

    class Meta:
        model = Profile
        
