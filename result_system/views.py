from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from adminpenal.models import Student


def get_logged_in_student(request):

    student_id = request.session.get('student_id')

    if not student_id:
        return None

    try:
        return Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        request.session.pop('student_id', None)
        return None


def get_result_context(student):

    subjects = [
        ('C', student.c),
        ('C++', student.cpp),
        ('Java', student.java),
        ('Python', student.python),
        ('HTML', student.html),
        ('CSS', student.css),
        ('SQL', student.sql),
    ]

    total = sum(marks for subject, marks in subjects)
    percentage = total / len(subjects)
    is_pass = all(marks >= 33 for subject, marks in subjects)

    return {
        'student': student,
        'subjects': subjects,
        'total': total,
        'percentage': percentage,
        'is_pass': is_pass,
    }


# LOGIN PAGE
def login(request):

    if request.method == "POST":

        email = request.POST.get('email')
        phone = request.POST.get('phone')

        try:

            student = Student.objects.get(
                student_email=email,
                student_phone=phone
            )

            # save student id in session
            request.session['student_id'] = student.id

            return redirect('dashboard')

        except Student.DoesNotExist:

            messages.error(request, "Invalid Email or Phone Number")

            return redirect('login')

    return render(request, 'login.html')

def dashboard(request):

    student = get_logged_in_student(request)

    if not student:
        return redirect('login')

    return render(request, 'student_dashboard.html', get_result_context(student))


def info(request):

    student = get_logged_in_student(request)

    if not student:
        return redirect('login')

    return render(request, 'info.html', {'student': student})


def result(request):

    student = get_logged_in_student(request)

    if not student:
        return redirect('login')

    return render(request, 'result.html', get_result_context(student))


def download_result(request):

    student = get_logged_in_student(request)

    if not student:
        return redirect('login')

    context = get_result_context(student)
    status = 'PASS' if context['is_pass'] else 'FAIL'

    lines = [
        'Student Result',
        f"Student ID: {student.id}",
        f"Name: {student.student_name}",
        f"Email: {student.student_email}",
        '',
        'Subject Marks',
    ]

    for subject, marks in context['subjects']:
        lines.append(f'{subject}: {marks}')

    lines.extend([
        '',
        f"Total: {context['total']} / 700",
        f"Percentage: {context['percentage']:.2f}%",
        f"Status: {status}",
    ])

    response = HttpResponse('\n'.join(lines), content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="result_{student.id}.txt"'

    return response


def logout_view(request):

    request.session.pop('student_id', None)

    return redirect('login')

def contact(request):
    return render(request, 'contact.html')

