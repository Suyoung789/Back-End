# Generated by Django 2.2.1 on 2019-06-04 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymove',
            name='possible_date',
            field=models.TextField(default=0),
        ),
    ]
