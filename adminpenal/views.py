from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Student

def login(request):

    if request.method == 'POST':

        username = request.POST.get("teacher_id")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            auth_login(request, user)
            return redirect('admin_dashbord')

        else:

            return render(request, "adminpenal/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, 'adminpenal/login.html')


def forgot_password(request):
    return render(request, 'adminpenal/forget_pass.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')


def admin_dashbord(request):
    return render(request, "adminpenal/admin_dashbord.html")


def add_student(request):

    if request.method == "POST":
        
        Student.objects.create(
            student_name = request.POST.get('student_name'),
            
            student_phone = request.POST.get('student_phone'),
            
            student_email = request.POST.get('student_email'),

            student_aadhar = request.FILES.get('student_aadhar'),

            student_photo = request.FILES.get('student_photo'),

            c = request.POST.get('c'),

            cpp = request.POST.get('cpp'),

            java = request.POST.get('java'),

            python = request.POST.get('python'),

            html = request.POST.get('html'),

            css = request.POST.get('css'),

            sql = request.POST.get('sql')

        )

        return redirect('/adminpenal/students/')

    return render(request,'adminpenal/add_student.html')

def students(request):

    data = Student.objects.all()

    return render(request,'adminpenal/students.html',{'data':data})


def results(request):

    data = Student.objects.all()

    return render(request,'adminpenal/results.html',{'data':data})



#   UPDATE......................AND.................DELETE....................

def update_student(request, id):

    data = get_object_or_404(Student, id=id)

    if request.method == "POST":

        data.student_name = request.POST.get('student_name')
        data.student_email = request.POST.get('student_email')
        data.student_phone = request.POST.get('student_phone')

        data.c = request.POST.get('c')
        data.cpp = request.POST.get('cpp')
        data.java = request.POST.get('java')
        data.python = request.POST.get('python')
        data.html = request.POST.get('html')
        data.css = request.POST.get('css')
        data.sql = request.POST.get('sql')

        if request.FILES.get('student_photo'):
            data.student_photo = request.FILES.get('student_photo')

        if request.FILES.get('student_aadharcard'):
            data.student_aadharcard = request.FILES.get('student_aadharcard')
        data.save()

        return redirect('students')

    return render(request, 'adminpenal/add_student.html', {'data': data})


def delete_student(request, id):

    data = get_object_or_404(Student, id=id)

    data.delete()

    return redirect('students')

def info(request, id=None):

    if id:
        data = [get_object_or_404(Student, id=id)]
    else:
        data = Student.objects.all()

    return render(request, 'adminpenal/info.html', {'data': data})
