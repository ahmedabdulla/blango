# Generated by Django 3.2.5 on 2023-04-09 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20230405_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autho',
            new_name='author',
        ),
    ]
