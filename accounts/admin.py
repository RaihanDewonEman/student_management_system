from django.contrib import admin
# from .models_all.administrative_officer import AdministrativeOfficer
# from .models_all.students import Student
# from .models_all.teachers import Teacher
# # Register your models here.
from accounts.models import Teacher, Student, User
from accounts.models.course import Course
from accounts.models.custom_user import AdministrativeOfficer

admin.site.register(User)
admin.site.register(AdministrativeOfficer)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
