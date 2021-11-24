from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.views.generic import ListView
from accounts.models.course import Course


class CourseList(LoginRequiredMixin, ListView):
    template_name = 'accounts/course_list.html'
    login_url = '/login/'
    model = Course
    queryset = None
    ordering = ['code']
    paginate_by = 10

    # def get_queryset(self):
    #     if self.queryset is not None:
    #         queryset = self.queryset
    #         if isinstance(queryset, QuerySet):
    #             queryset = queryset.all()
    #     elif self.model is not None:
    #         queryset = self.model.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super(CourseList, self).get_context_data(**kwargs)
    #     return context



