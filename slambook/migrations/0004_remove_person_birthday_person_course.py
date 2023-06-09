# Generated by Django 4.2.1 on 2023-06-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slambook', '0003_person_motto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='birthday',
        ),
        migrations.AddField(
            model_name='person',
            name='course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]