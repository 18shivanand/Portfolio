# Generated by Django 4.0 on 2022-04-11 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogs_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs',
            new_name='Blog',
        ),
    ]
