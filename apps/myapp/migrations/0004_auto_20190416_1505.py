# Generated by Django 2.1.4 on 2019-04-16 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190416_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
