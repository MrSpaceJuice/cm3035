from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
# Extends the base Django user model.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=256, null=True, blank=True)
    teacher = models.BooleanField(null=False, default=False)
    picture = models.FileField(upload_to='static/profile-pictures/', null=True, default="static/placeholder.jpg")
    
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() 

class Course(models.Model):
    course = models.CharField(max_length=256, null=False, blank=False)
    name = models.CharField(max_length=256, null=False, blank=False)
    teacher = models.ForeignKey(User, related_name='teacher', on_delete=models.CASCADE)
    student = models.ManyToManyField(Profile, related_name='student', through='CourseUserLink')

    def __str__(self):
        return self.course

class CourseMaterials(models.Model):

    material = models.FileField(upload_to='static/course-materials/')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def __str__(self):
        return os.path.basename(self.material.name)

class Deadline(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    event = models.CharField(max_length=256, null=False, blank=False)
    event_date = models.DateTimeField(null=False, blank=False)

class CourseUserLink(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=256, null=True, blank=True)

