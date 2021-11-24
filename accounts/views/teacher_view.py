from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from accounts.Form.teacher_form import TeacherForm
from accounts.models import User, Teacher


class TeacherView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    template_name = 'accounts/teacher_form.html'
    form_class = TeacherForm
    success_url = 'home_page'

    def get_success_url(self):
        return reverse(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(TeacherView, self).get_context_data()
        context['form'] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            print("invalid")
            return self.form_invalid(form)


