from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse

from .models import Course, Step

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses':courses})

    #these lines were changed to use render template instead
    #"""make this output into a list of strings"""
    #output = ','.join([str(course) for course in courses])
    #return HttpResponse(output)

def course_detail(request, pk):
    # need to get a course with a given pk
    # and render the template
    # Model.get(attr=value) gets a single Model instance by a given attribute (pk in this case)

    # course = Course.objects.get(pk=pk)   chaged to get_object_404
    #if it's not a Course object entered, it'll 404
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})
