# Generated by Django 5.0 on 2024-01-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='stage',
            field=models.IntegerField(null=True),
        ),
    ]