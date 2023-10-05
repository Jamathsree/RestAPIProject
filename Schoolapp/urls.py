from . import views
from django.urls import path

urlpatterns=[
    path("",views.school,name='school'),
    path("student_list",views.student_list,name='student_list'),
    path("student_detail/<int:pk>/",views.student_detail,name='student_detail'),
]

