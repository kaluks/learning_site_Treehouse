# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from .models import Course, Step


class CourseModeTests(TestCase):
    def test_course_creation(self):
        course=Course.objects.create(
            title="Python Regular Expressions",
            description = "Learn to write regular expressions"
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)
