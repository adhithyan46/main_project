# Generated by Django 5.1 on 2024-09-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_preferred_loc_userprofile_interests_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='interests',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
