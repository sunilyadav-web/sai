# Generated by Django 4.0.1 on 2022-09-27 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_examandaccounthide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examandaccounthide',
            old_name='display_Account',
            new_name='display_account',
        ),
        migrations.RenameField(
            model_name='examandaccounthide',
            old_name='display_Exam',
            new_name='display_exam',
        ),
    ]
