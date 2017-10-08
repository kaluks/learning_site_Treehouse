# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default =0) #lets us control the order of steps
    course = models.ForeignKey(Course) #FK is a column that points to a record in another table
        #this way a single course can have multiple steps

    class Meta:
        ordering = ['order',]
        # orders steps so know what order to watch videos/instances
        # if theres a conflict or order not stated, django will order by id

    def __str__(self):
        return self.title  # thi is so we can print it out
