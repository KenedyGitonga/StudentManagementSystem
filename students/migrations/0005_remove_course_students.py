# Generated by Django 4.2.4 on 2023-11-28 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_course_course_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
    ]
