from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse

from .models import Student, Course
from .forms import StudentForm, CourseForm


# Create your views here.
def index(request):
  return render(request, 'students/index.html', {
    'students': Student.objects.all(),
    'courses': Course.objects.all(),  # Add courses to the context
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))


def add(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': form
  })


def edit(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })


def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))


# views for courses
def course_index(request):
  return render(request, 'students/courses.html', {
    'courses': Course.objects.all(),
  })

def view_course(request, id):
  return HttpResponseRedirect(reverse('course_index'))

def add_course(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('course_index')

  else:
    form = CourseForm()
  return render(request, 'students/add_course.html', {
    'form': form,
  })

def edit_course(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit_course.html', {
                'form': form,
                'success': True,
                'course': course,  # Include course in the context
            })
    else:
        form = CourseForm(instance=course)

    return render(request, 'students/edit_course.html', {
        'form': form,
        'course': course,  # Include course in the context
    })

def delete_course(request, id):
  if request.method == 'POST':
    course = Course.objects.get(pk=id)
    course.delete()
  return HttpResponseRedirect(reverse('course_index'))
