from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from grades.models import Student


def index(request):
    return render(request, 'grades/index.html')


def register(request):
    name = request.POST['name']
    student = Student(name=name)
    student.save()

    grade1 = float(request.POST['grade1'])
    grade2 = float(request.POST.get('grade2'))
    grade3 = float(request.POST['grade3'])

    student.grade_set.create(value=grade1)
    student.grade_set.create(value=grade2)
    student.grade_set.create(value=grade3)

    return HttpResponseRedirect(reverse('grades:success'))


def success(request):
    return render(request, 'grades/success.html')


def reports(request):
    students = Student.objects.all()

    return render(
        request,
        'grades/reports.html',
        {'students_list': students}
    )
