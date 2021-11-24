from django.db import models

from accounts.models import Student


class Taken(models.Model):
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.CharField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
