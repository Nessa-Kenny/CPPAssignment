# Generated by Django 2.0.2 on 2020-11-27 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_recipe',
            old_name='text',
            new_name='Title',
        ),
    ]
