# Generated by Django 3.1 on 2021-11-10 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20211110_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='likedin_profile',
            new_name='linkedin_profile',
        ),
    ]
