from django.urls import path

from .views.course_list import CourseList
from .views.course_view import CourseView
from .views.login_views import LoginView, LogoutView
from .views.home_views import HomeView
from .views.profile_view import ProfileView
from .views.student_list_view import StudentList
from .views.student_view import StudentView
from .views.teacher_view import TeacherView
from .views.user_view import UserView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<pk>/', ProfileView.as_view(), name='profile'),
    path('createstudent/', StudentView.as_view(), name='student'),
    path('createteacher/', TeacherView.as_view(), name='teacher'),
    path('createcourse/', CourseView.as_view(), name='course'),
    path('courselist/', CourseList.as_view(), name='course_list'),
    path('studentlist/', StudentList.as_view(), name='student_list'),
    path('createuser/', UserView.as_view(), name='create_user'),
]
