# Generated by Django 4.0.1 on 2022-09-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_profile_created_at_profile_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamAndAccountHide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_Exam', models.BooleanField(default=False)),
                ('display_Account', models.BooleanField(default=False)),
            ],
        ),
    ]