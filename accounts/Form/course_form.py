from django.forms import ModelForm
from django import forms

from accounts.models.course import Course


class CourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        self.fields['code'] = forms.CharField(label='Course Code', required=True)
        self.fields['title'] = forms.CharField(label='Course Title', required=False)
        self.fields['credit'] = forms.IntegerField(label='Course Credit', initial = 3, required=False)
        self.fields['semester'] = forms.IntegerField(label='Semester No', required=True)

    class Meta:
        model = Course
        fields = ['code', 'title', 'credit', 'semester']



