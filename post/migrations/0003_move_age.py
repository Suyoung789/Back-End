# Generated by Django 2.2.1 on 2019-06-03 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20190603_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='move',
            name='age',
            field=models.CharField(default=0, max_length=10),
        ),
    ]