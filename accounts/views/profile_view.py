from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from accounts.models import User


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    template_name = 'accounts/profile.html'
    model = User


