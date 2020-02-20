# Generated by Django 2.2.8 on 2020-02-18 09:51

import cv.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv_id', models.IntegerField(null=True)),
                ('wants_verification', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('cv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='cv.CV')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year_start', models.PositiveIntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1990), cv.models.max_value_current_year])),
                ('year_end', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1990), cv.models.max_value_current_year])),
                ('additional_info', models.CharField(max_length=150, null=True)),
                ('cv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='cv.CV')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('level', models.CharField(max_length=20)),
                ('cv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='languages', to='cv.CV')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_info', models.TextField()),
                ('schools', models.TextField()),
                ('experiences', models.TextField()),
                ('skills', models.TextField()),
                ('languages', models.TextField()),
                ('cv', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='cv.CV')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('year_start', models.PositiveIntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1990), cv.models.max_value_current_year])),
                ('year_end', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1990), cv.models.max_value_current_year])),
                ('cv', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='cv.CV')),
            ],
        ),
        migrations.CreateModel(
            name='BasicInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('picture', models.ImageField(upload_to='cv_pictures/')),
                ('phone_number', models.CharField(max_length=12)),
                ('date_of_birth', models.CharField(max_length=12)),
                ('cv', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basic_info', to='cv.CV')),
            ],
        ),
    ]
