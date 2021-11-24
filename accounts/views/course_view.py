from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView

from accounts.Form.course_form import CourseForm


class CourseView(LoginRequiredMixin, FormView):
    template_name = 'accounts/course_form.html'
    login_url = '/login/'
    success_url = 'home_page'
    form_class = CourseForm

    def get_success_url(self):
        return reverse(self.success_url)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect(self.get_success_url())
        # return self.form_valid(form)
        else:
            return self.form_invalid(form)
