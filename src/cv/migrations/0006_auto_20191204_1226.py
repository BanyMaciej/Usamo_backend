# Generated by Django 2.2.7 on 2019-12-04 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20191204_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='user_id',
            new_name='cv_id',
        ),
    ]
