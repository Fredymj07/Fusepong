# Generated by Django 3.2.6 on 2021-08-25 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_ticket_uploadedfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='uploadedFile',
            new_name='uploaded_file',
        ),
    ]
