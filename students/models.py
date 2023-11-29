from django.db import models


# Create your models here.
class Student(models.Model):
  student_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  field_of_study = models.CharField(max_length=50)
  gpa = models.FloatField()

  def __str__(self):
    return f'Student: {self.first_name} {self.last_name}'


class Course(models.Model):
  course_code = models.CharField(max_length=20)
  course_name = models.CharField(max_length=100)
  instructor = models.CharField(max_length=100)
  schedule = models.CharField(max_length=100)
  credits = models.IntegerField()

  def __str__(self):
    return f'Course: {self.course_code} - {self.course_name}'


