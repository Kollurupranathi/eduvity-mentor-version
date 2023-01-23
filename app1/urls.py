from django.urls import path
from . import views

urlpatterns = [
    path('',views.Sign_up,name="Sign_up"),
    path('answer/',views.answer, name="answer"),
    path('login/',views.login, name="login"),
    path('loginn/',views.login, name="login"),
    path('logged/',views.logged, name="logged"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('<int:course_id>', views.course, name="course")
]
