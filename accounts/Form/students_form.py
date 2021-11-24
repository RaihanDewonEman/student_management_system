from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from accounts.enums.user_type_enum import StatusBEnum
from accounts.models import Student


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.fields['student_id'] = forms.CharField(label='Student ID', error_messages={
            'required': "Student ID should be less than 10 characters"
        }, required=True)
        self.fields['registration_number'] = forms.CharField(label='Registration No', required=True)
        self.fields['session'] = forms.CharField(label='Session', required=True)
        self.fields['roll_number'] = forms.CharField(label='Roll No', error_messages={
            'required': "Student Roll should be 6 characters"
        }, required=True)
        self.fields['academic_year'] = forms.CharField(label='Academic Year', required=True)

    class Meta:
        model = Student
        fields = [
            'student_id', 'registration_number', 'roll_number',
            'session', 'academic_year', 'user'
        ]
