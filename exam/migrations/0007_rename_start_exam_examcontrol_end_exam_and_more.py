# Generated by Django 4.0.5 on 2022-08-01 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_rename_start_examcontrol_start_exam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examcontrol',
            old_name='start_exam',
            new_name='end_exam',
        ),
        migrations.AddField(
            model_name='examcontrol',
            name='start_start',
            field=models.BooleanField(default=False),
        ),
    ]
