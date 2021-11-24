from django import forms

from accounts.models import User


class LoginForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__( *args, **kwargs)

        self.fields['email'] = forms.EmailField(label='Email', required=True,
                                                widget=forms.TextInput(
                                                    attrs={'Size': '30', 'placeholder': '2016-014-439@cs.du.ac.bd'}))
        self.fields['password'] = forms.CharField(label='Password', required=True,
                                                  widget=forms.PasswordInput(
                                                      attrs={'Size': '30', 'placeholder': 'Enter your password'}))

    class Meta:
        model = User
        fields = ['email', 'password']
