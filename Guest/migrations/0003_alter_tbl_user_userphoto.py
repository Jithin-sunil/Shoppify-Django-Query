# Generated by Django 5.0.6 on 2024-06-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_rename_user_tbl_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_user',
            name='userphoto',
            field=models.FileField(upload_to='Assets/UserPhoto/'),
        ),
    ]
