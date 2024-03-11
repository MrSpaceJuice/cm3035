from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CourseUserLinkInline(admin.TabularInline):
    model = CourseUserLink
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    inlines = [CourseUserLinkInline]

class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('course', 'name', 'teacher')

class DeadlineAdmin(admin.ModelAdmin):
    model = Deadline
    list_display = ('course', 'event', 'event_date')

class CourseMaterialsAdmin(admin.ModelAdmin):
    model = CourseMaterials

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Deadline, DeadlineAdmin)
admin.site.register(CourseMaterials, CourseMaterialsAdmin)