# Generated by Django 4.0 on 2024-03-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0005_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(default='', null=True, upload_to='static/profile-pictures/'),
        ),
    ]
