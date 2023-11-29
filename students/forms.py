from django import forms
from .models import Student, Course


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
    labels = {
      'student_number': 'Student Number',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'field_of_study': 'Field of Study',
      'gpa': 'GPA'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
    }

class CourseForm(forms.ModelForm):
  class Meta:
    model = Course   # Use the Course model
    fields = ['course_code', 'course_name', 'instructor', 'schedule', 'credits']
    labels = {
      'course_code': 'Course Code',
      'course_name': 'Course Name',
      'instructor': 'Instructor',
      'schedule': 'Schedule',
      'credits': 'Credits',
    }
    widgets = {
      'course_code': forms.TextInput(attrs={'class': 'form-control'}),
      'course_name': forms.TextInput(attrs={'class': 'form-control'}),
      'instructor': forms.TextInput(attrs={'class': 'form-control'}),
      'schedule': forms.TextInput(attrs={'class': 'form-control'}),
      'credits': forms.NumberInput(attrs={'class': 'form-control'}),
    }



