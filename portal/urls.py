from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student, name='student'),
    path('parent/', views.parent, name='parent'),
    path('staff/', views.staff, name='staff'),
    path('student/list', views.complain_list, name='complain_list'),
    path('student/<int:pk>/', views.complain_detail, name='complain_detail'),
]