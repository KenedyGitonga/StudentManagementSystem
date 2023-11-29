from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<int:id>', views.view_student, name='view_student'),
  path('add/', views.add, name='add'),
  path('edit/<int:id>/', views.edit, name='edit'),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('courses/', views.course_index, name='course_index'),
  path('courses/<int:id>/', views.view_course, name='view_course'),
  path('courses/add/', views.add_course, name='add_course'),
  path('courses/edit/<int:id>/', views.edit_course, name='edit_course'),
  path('courses/delete/<int:id>/', views.delete_course, name='delete_course'),
]