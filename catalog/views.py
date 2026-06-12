from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseForm
from .models import Category, Coach, Course


def home(request):
    featured_courses = Course.objects.select_related('category', 'coach').filter(is_available=True)[:3]
    context = {
        'featured_courses': featured_courses,
        'course_count': Course.objects.count(),
        'category_count': Category.objects.count(),
        'coach_count': Coach.objects.filter(is_active=True).count(),
        'categories': Category.objects.prefetch_related('courses'),
    }
    return render(request, 'catalog/home.html', context)


def course_list(request):
    courses = Course.objects.select_related('category', 'coach')
    return render(request, 'catalog/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(
        Course.objects.select_related('category', 'coach', 'coach__profile').prefetch_related('members'),
        pk=pk,
    )
    return render(request, 'catalog/course_detail.html', {'course': course})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, f'"{course.title}" was added to the catalog.')
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm()

    return render(request, 'catalog/course_form.html', {'form': form})


def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        title = course.title
        course.delete()
        messages.success(request, f'"{title}" was removed from the catalog.')
        return redirect('course_list')

    return render(request, 'catalog/course_confirm_delete.html', {'course': course})

# Create your views here.
