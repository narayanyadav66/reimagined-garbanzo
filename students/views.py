
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count
from django.core.paginator import Paginator
from django.http import HttpResponse
from openpyxl import Workbook
import csv

from .models import Student
from .forms import StudentForm


def filtered_students(request):
    students = Student.objects.all()

    search_query = request.GET.get('search', '').strip()
    course_filter = request.GET.get('course', '').strip()
    min_marks = request.GET.get('min_marks', '').strip()
    max_marks = request.GET.get('max_marks', '').strip()

    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) |
            Q(roll_number__icontains=search_query) |
            Q(course__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    if course_filter:
        students = students.filter(course=course_filter)

    if min_marks:
        try:
            value = float(min_marks)
            if 0 <= value <= 100:
                students = students.filter(marks__gte=value)
        except ValueError:
            pass

    if max_marks:
        try:
            value = float(max_marks)
            if 0 <= value <= 100:
                students = students.filter(marks__lte=value)
        except ValueError:
            pass

    return students.order_by('name')


@login_required
def dashboard(request):
    all_students = filtered_students(request)

    # Keep the full filtered result for statistics and the chart.
    chart_students = list(all_students)
    total_filtered = len(chart_students)

    paginator = Paginator(all_students, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    topper = Student.objects.order_by('-marks', 'name').first()

    average_marks = Student.objects.aggregate(
        average=Avg('marks')
    )['average']

    course_stats = (
        Student.objects.values('course')
        .annotate(total=Count('id'))
        .order_by('course')
    )

    context = {
        'students': page_obj,
        'page_obj': page_obj,
        'total_students': Student.objects.count(),
        'topper': topper,
        'average_marks': average_marks,
        'course_stats': course_stats,
        'search_query': request.GET.get('search', '').strip(),
        'course_filter': request.GET.get('course', '').strip(),
        'min_marks': request.GET.get('min_marks', '').strip(),
        'max_marks': request.GET.get('max_marks', '').strip(),
        'courses': Student.objects.values_list(
            'course', flat=True
        ).distinct().order_by('course'),
        'chart_students': chart_students,
        'total_filtered': total_filtered,
    }

    return render(request, 'students/dashboard.html', context)


@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            student = form.save()
            messages.success(
                request, f'Student {student.name} added successfully.'
            )
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add Student',
    })


@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Edit Student',
    })


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        name = student.name
        student.delete()
        messages.success(request, f'Student {name} deleted successfully.')
        return redirect('dashboard')

    return render(request, 'students/student_confirm_delete.html', {
        'student': student,
    })


@login_required
def export_csv(request):
    students = filtered_students(request)

    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = (
        'attachment; filename="students.csv"'
    )
    response.write('\ufeff')

    writer = csv.writer(response)
    writer.writerow([
        'Roll Number', 'Name', 'Email', 'Age', 'Course', 'Marks'
    ])

    for student in students:
        writer.writerow([
            student.roll_number,
            student.name,
            student.email,
            student.age,
            student.course,
            student.marks,
        ])

    return response


@login_required
def export_excel(request):
    students = filtered_students(request)

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Students'

    sheet.append([
        'Roll Number', 'Name', 'Email', 'Age', 'Course', 'Marks'
    ])

    for student in students:
        sheet.append([
            student.roll_number,
            student.name,
            student.email,
            student.age,
            student.course,
            student.marks,
        ])

    response = HttpResponse(
        content_type=(
            'application/vnd.openxmlformats-officedocument.'
            'spreadsheetml.sheet'
        )
    )
    response['Content-Disposition'] = (
        'attachment; filename="students.xlsx"'
    )

    workbook.save(response)
    return response
