# Generated by Django 3.2.8 on 2021-11-03 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211103_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
