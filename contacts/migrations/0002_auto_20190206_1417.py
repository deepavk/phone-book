# Generated by Django 2.1.5 on 2019-02-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='last_name',
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['name', 'email'], name='contacts_co_name_85459a_idx'),
        ),
    ]
