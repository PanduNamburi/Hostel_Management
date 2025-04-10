# Generated by Django 5.2 on 2025-04-10 22:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('parent_email', models.EmailField(max_length=254)),
                ('outing_reason', models.TextField(blank=True, max_length=200)),
                ('outing_time', models.DateTimeField()),
                ('return_time', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('requested_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
