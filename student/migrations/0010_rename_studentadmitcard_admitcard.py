# Generated by Django 4.0.1 on 2022-08-19 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_studentadmitcard_delete_admitcard'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentAdmitCard',
            new_name='AdmitCard',
        ),
    ]
