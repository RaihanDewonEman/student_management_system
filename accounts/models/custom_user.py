from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# from StudentManagementSystem import settings
from accounts.models.user import User


class Student(models.Model):
    student_id = models.CharField(max_length=9, unique=True)
    registration_number = models.CharField(max_length=10)
    roll_number = models.CharField(max_length=6)
    session = models.CharField(max_length=7)
    academic_year = models.CharField(max_length=5)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=8, unique=True)
    room_number = models.CharField(max_length=5)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class AdministrativeOfficer(models.Model):
    admin_id = models.CharField(max_length=8, unique=True)
    designation = models.CharField(max_length=30)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_student(sender, instance, **kwargs):
    instance.student.save()
