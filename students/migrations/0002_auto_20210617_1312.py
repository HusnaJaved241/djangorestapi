# Generated by Django 3.1.6 on 2021-06-17 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Students',
        ),
    ]