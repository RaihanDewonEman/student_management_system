from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from accounts.enums.user_type_enum import StatusBEnum
from accounts.models import Teacher


class TeacherForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

        # self.fields['first_name'] = forms.CharField(label='First Name', required=True)
        # self.fields['last_name'] = forms.CharField(label='Last Name', required=True)
        # self.fields['phone_number'] = forms.CharField(label='Phone Number', required=True)
        # self.fields['email'] = forms.CharField(label='Email', required=True)
        # self.fields['dob'] = forms.CharField(label='Date of Birth', widget=AdminDateWidget, required=True)
        # self.fields['address'] = forms.CharField(label='Address', required=True)
        # self.fields['type'] = forms.ChoiceField(label='Account Type', choices= StatusBEnum.choice_list(), required=True)
        self.fields['room_number'] = forms.CharField(label='Room No', required=True)
        #self.fields['avatar'] = forms.ImageField(label= 'Photo')

    class Meta:
        model = Teacher
        fields = [
            'room_number',
        ]
