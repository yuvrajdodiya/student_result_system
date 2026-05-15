from django.urls import path
from . import views

urlpatterns = [

    path("login/", views.login, name="login"),

    path("logout/", views.logout_view, name="logout"),

    path('forgot_password/', views.forgot_password, name='forgot_password'),

    path('admin_dashbord/', views.admin_dashbord, name='admin_dashbord'),

    path('add_student/',views.add_student ,name='add_student'),

    path('students/',views.students,name='students'),

    path('results/',views.results,name='results'),

    path('info/',views.info, name='info'),

    path('info/<int:id>/',views.info, name='admin_student_info'),
    
# update and delete
    path('update_student/<int:id>/', views.update_student, name='update_student'),
    
    path('delete_student/<int:id>/', views.delete_student, name='delete_student'),

]
