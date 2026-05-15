from django.urls import path
from . import views

urlpatterns = [

    path("login/", views.login, name="login"),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('info/', views.info, name='student_info'),

    path('result/', views.result, name='student_result'),

    path('result/download/', views.download_result, name='download_result'),

    path('logout/', views.logout_view, name='student_logout'),

    path('contact/', views.contact, name='contact')


]
