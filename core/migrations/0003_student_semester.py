# Generated by Django 4.2.2 on 2023-06-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.CharField(default='1', max_length=2),
        ),
    ]
