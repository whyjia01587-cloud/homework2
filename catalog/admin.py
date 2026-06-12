from django.contrib import admin

from .models import Category, Coach, CoachProfile, Course, Member


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')


class CoachProfileInline(admin.StackedInline):
    model = CoachProfile
    extra = 0


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'experience_years', 'is_active')
    list_filter = ('is_active', 'specialization')
    search_fields = ('full_name', 'specialization')
    inlines = [CoachProfileInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'coach', 'difficulty', 'price', 'start_date', 'is_available')
    list_filter = ('category', 'difficulty', 'is_available', 'start_date')
    search_fields = ('title', 'description', 'coach__full_name')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'joined_date')
    search_fields = ('full_name', 'email')
    filter_horizontal = ('courses',)
