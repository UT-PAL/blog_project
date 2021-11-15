# Generated by Django 3.1 on 2021-11-07 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
