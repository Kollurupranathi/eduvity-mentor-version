# Generated by Django 4.1.2 on 2023-01-23 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_alter_courses_course_createdat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluations',
            old_name='projectName',
            new_name='projectname',
        ),
        migrations.AlterField(
            model_name='courses',
            name='Course_createdAt',
            field=models.DateField(default=datetime.datetime(2023, 1, 23, 17, 38, 54, 842765)),
        ),
    ]