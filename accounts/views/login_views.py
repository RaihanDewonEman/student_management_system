from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView
from accounts.Form.login_form import LoginForm
from django.views.generic import RedirectView


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login_form.html'
    success_url = 'home_page'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data()
        context['form'] = self.form_class()
        return context

    def get_success_url(self):
        return reverse(self.success_url)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # print(self.get_success_url())
            return redirect(self.get_success_url())
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # if form.is_valid():
        user = authenticate(email=form['email'].data, password=form['password'].data)
        if user is not None:
            login(request, user)
            return redirect(self.get_success_url())
        return render(request, self.template_name, self.get_context_data())


class LogoutView(RedirectView):
    url = 'login_page'

    def get_success_url(self):
        return reverse(self.url)

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.get_success_url())
