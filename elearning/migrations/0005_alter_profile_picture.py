# Generated by Django 4.0 on 2024-03-11 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0004_remove_course_material_coursematerials_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='static/profile-pictures/'),
        ),
    ]
