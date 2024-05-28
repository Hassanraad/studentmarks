# Generated by Django 5.0 on 2024-01-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('fname', models.CharField(max_length=25)),
                ('grades', models.CharField(max_length=25)),
                ('subjects', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stages', models.IntegerField()),
                ('department', models.CharField(max_length=25)),
                ('studentID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('studentID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('academic_year', models.CharField(default='', max_length=100)),
                ('stage', models.IntegerField(default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects1', models.CharField(default='', max_length=100)),
                ('subjects2', models.CharField(default='', max_length=100)),
                ('subjects3', models.CharField(default='', max_length=100)),
                ('subjects4', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
