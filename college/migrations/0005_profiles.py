# Generated by Django 5.0.6 on 2024-05-28 15:39

import college.utlas
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0004_alter_grade_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, null=True, upload_to=college.utlas.user_directory_path)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
    ]
