# Generated by Django 2.1.4 on 2019-04-16 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_pet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='myapp.User'),
            preserve_default=False,
        ),
    ]
