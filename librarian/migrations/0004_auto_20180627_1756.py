# Generated by Django 2.0 on 2018-06-27 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarian', '0003_auto_20180627_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='shelf_store_no',
            new_name='shelf_no',
        ),
    ]
