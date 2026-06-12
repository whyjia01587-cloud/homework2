from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Coach(models.Model):
    full_name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    experience_years = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class CoachProfile(models.Model):
    coach = models.OneToOneField(Coach, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    certification = models.CharField(max_length=200)
    photo_url = models.URLField(blank=True)

    def __str__(self):
        return f'{self.coach.full_name} profile'


class Course(models.Model):
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'

    DIFFICULTY_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    title = models.CharField(max_length=180)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='courses')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default=BEGINNER)
    duration_minutes = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    start_date = models.DateField()
    is_available = models.BooleanField(default=True)
    image_url = models.URLField(blank=True)

    class Meta:
        ordering = ['start_date', 'title']

    def __str__(self):
        return self.title


class Member(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    joined_date = models.DateField(default=timezone.now)
    courses = models.ManyToManyField(Course, related_name='members', blank=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name
