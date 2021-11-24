from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views.generic import ListView

from accounts.models import Student


class StudentList(LoginRequiredMixin, ListView):
    template_name = 'accounts/student_list.html'
    login_url = '/login/'
    model = Student
    queryset = None
    ordering = ['user_id']
    paginate_by = 10
