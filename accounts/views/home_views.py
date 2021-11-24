from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/homepage.html'
    login_url = '/login/'
    # redirect_field_name = 'home_page'

