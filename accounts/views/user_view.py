from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from accounts.Form.user_form import UserForm
from accounts.enums.user_type_enum import StatusBEnum
from accounts.models import User


class UserView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    template_name = 'accounts/user_form.html'
    form_class = UserForm
    success_url = ''

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = User.objects.create_user(first_name=form['first_name'].data, last_name=form['last_name'].data,
                                            phone_number=form['phone_number'].data, email=form['email'].data,
                                            dob=form['dob'].data, address=form['address'].data, type=form['type'].data,
                                            password=form['password'].data)
            if user.type == StatusBEnum.STUDENT.value:
                self.success_url = 'student'
            elif user.type == StatusBEnum.TEACHER.value:
                self.success_url = 'teacher'
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
