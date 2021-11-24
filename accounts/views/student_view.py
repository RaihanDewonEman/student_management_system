from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from accounts.Form.students_form import StudentForm
from accounts.models import User, Student


class StudentView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    template_name = 'accounts/student_form.html'
    form_class = StudentForm
    success_url = 'home_page'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            # User.student.student_id = form['student_id']
            # User.student.academic_year = form['academic_year']
            # User.student.session = form['session']
            # User.student.registration_number = form['registration_number']
            # User.student.roll_number = form['roll_number']

            # user.objects.create_user()
            # Student.user_id = user.id
            #
            # user.save()
            # form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
