# Generated by Django 2.2 on 2020-07-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
