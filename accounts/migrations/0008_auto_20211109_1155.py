# Generated by Django 3.2.8 on 2021-11-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativeofficer',
            name='admin_id',
            field=models.CharField(default=101023, max_length=8, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='student_id',
            field=models.CharField(default=299456, max_length=8, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.CharField(default=46385, max_length=8, unique=True),
            preserve_default=False,
        ),
    ]
