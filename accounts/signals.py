# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from accounts.models import Student, User, Teacher
# from accounts.models.custom_user import AdministrativeOfficer
#
#
# @receiver(post_save, sender=User)
# def create_user_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_student(sender, instance, **kwargs):
#     instance.student.save()


# @receiver(post_save, sender=User)
# def create_user_teacher(sender, instance, created, **kwargs):
#     if created and User.type == 2:
#         Teacher.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_user_teacher(sender, instance, created, **kwargs):
#     instance.teacher.save()
#
#
# @receiver(post_save, sender=User)
# def create_administrativeOfficer(sender, instance, created, **kwargs):
#     if created and User.type == 1:
#         AdministrativeOfficer.objects.create(user=instance)
#
#
# @receiver(post_save, sender=User)
# def save_administrativeOfficer(sender, instance, created, **kwargs):
#     instance.administrativeOfficer.save()
