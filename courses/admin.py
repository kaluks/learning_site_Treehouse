# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Course, Step

class StepInline(admin.StackedInline):
    model = Step
    #adding the StepInline and CourseAdmin
    #let's us see all the steps under each course
    #in the admin site of that course
    #and we can easiy add more steps from under that course, rather
    #than adding the step and picking the course from the dropdown menu


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Course, CourseAdmin)
# registers the Course model with the admin site
admin.site.register(Step)
