from datetime import date, timedelta
from decimal import Decimal

from django.core.management.base import BaseCommand

from catalog.models import Category, Coach, CoachProfile, Course, Member


class Command(BaseCommand):
    help = 'Create sample data for the fitness course catalog.'

    def handle(self, *args, **options):
        categories = {
            'Yoga': 'Flexibility, breathing, balance, and mindful strength classes.',
            'Strength': 'Resistance training focused on power, posture, and muscle tone.',
            'Cardio': 'High-energy classes for endurance, stamina, and heart health.',
            'Pilates': 'Controlled movement classes for core strength and mobility.',
        }

        category_objects = {
            name: Category.objects.update_or_create(
                name=name,
                defaults={'description': description},
            )[0]
            for name, description in categories.items()
        }

        coach_data = [
            {
                'full_name': 'Anna Petrova',
                'specialization': 'Yoga and mobility',
                'experience_years': 8,
                'bio': 'Anna designs calm but challenging classes for posture, mobility, and stress relief.',
                'certification': 'RYT-500 Yoga Alliance',
                'photo_url': 'https://images.unsplash.com/photo-1594381898411-846e7d193883?auto=format&fit=crop&w=600&q=80',
            },
            {
                'full_name': 'Mikhail Sokolov',
                'specialization': 'Strength conditioning',
                'experience_years': 10,
                'bio': 'Mikhail helps members build reliable technique before adding serious load.',
                'certification': 'Certified Strength and Conditioning Specialist',
                'photo_url': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?auto=format&fit=crop&w=600&q=80',
            },
            {
                'full_name': 'Elena Ivanova',
                'specialization': 'Cardio and functional training',
                'experience_years': 6,
                'bio': 'Elena leads upbeat group sessions that combine rhythm, intervals, and bodyweight drills.',
                'certification': 'ACE Group Fitness Instructor',
                'photo_url': 'https://images.unsplash.com/photo-1605296867304-46d5465a13f1?auto=format&fit=crop&w=600&q=80',
            },
            {
                'full_name': 'Sergey Orlov',
                'specialization': 'Pilates and rehabilitation fitness',
                'experience_years': 7,
                'bio': 'Sergey focuses on core control, safe movement patterns, and long-term body awareness.',
                'certification': 'Balanced Body Pilates Instructor',
                'photo_url': 'https://images.unsplash.com/photo-1549060279-7e168fcee0c2?auto=format&fit=crop&w=600&q=80',
            },
        ]

        coaches = {}
        for item in coach_data:
            coach, _ = Coach.objects.update_or_create(
                full_name=item['full_name'],
                defaults={
                    'specialization': item['specialization'],
                    'experience_years': item['experience_years'],
                    'is_active': True,
                },
            )
            CoachProfile.objects.update_or_create(
                coach=coach,
                defaults={
                    'bio': item['bio'],
                    'certification': item['certification'],
                    'photo_url': item['photo_url'],
                },
            )
            coaches[item['full_name']] = coach

        today = date.today()
        course_data = [
            {
                'title': 'Morning Yoga Flow',
                'description': 'A balanced yoga course for flexibility, breathing, and gentle strength.',
                'category': 'Yoga',
                'coach': 'Anna Petrova',
                'difficulty': Course.BEGINNER,
                'duration_minutes': 55,
                'price': Decimal('35.00'),
                'start_date': today + timedelta(days=3),
                'is_available': True,
                'image_url': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=900&q=80',
            },
            {
                'title': 'Power Strength Basics',
                'description': 'Foundational lifting technique with progressive full-body workouts.',
                'category': 'Strength',
                'coach': 'Mikhail Sokolov',
                'difficulty': Course.INTERMEDIATE,
                'duration_minutes': 70,
                'price': Decimal('48.00'),
                'start_date': today + timedelta(days=5),
                'is_available': True,
                'image_url': 'https://images.unsplash.com/photo-1534367610401-9f5ed68180aa?auto=format&fit=crop&w=900&q=80',
            },
            {
                'title': 'HIIT Cardio Burn',
                'description': 'Fast interval training for stamina, coordination, and calorie burn.',
                'category': 'Cardio',
                'coach': 'Elena Ivanova',
                'difficulty': Course.ADVANCED,
                'duration_minutes': 45,
                'price': Decimal('42.00'),
                'start_date': today + timedelta(days=7),
                'is_available': True,
                'image_url': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?auto=format&fit=crop&w=900&q=80',
            },
            {
                'title': 'Core Pilates Studio',
                'description': 'A precise Pilates program for core control, balance, and posture.',
                'category': 'Pilates',
                'coach': 'Sergey Orlov',
                'difficulty': Course.BEGINNER,
                'duration_minutes': 60,
                'price': Decimal('39.00'),
                'start_date': today + timedelta(days=10),
                'is_available': True,
                'image_url': 'https://images.unsplash.com/photo-1510894347713-fc3ed6fdf539?auto=format&fit=crop&w=900&q=80',
            },
        ]

        course_objects = {}
        for item in course_data:
            course, _ = Course.objects.update_or_create(
                title=item['title'],
                defaults={
                    'description': item['description'],
                    'category': category_objects[item['category']],
                    'coach': coaches[item['coach']],
                    'difficulty': item['difficulty'],
                    'duration_minutes': item['duration_minutes'],
                    'price': item['price'],
                    'start_date': item['start_date'],
                    'is_available': item['is_available'],
                    'image_url': item['image_url'],
                },
            )
            course_objects[item['title']] = course

        member_data = [
            {
                'full_name': 'Daria Smirnova',
                'email': 'daria@example.com',
                'courses': ['Morning Yoga Flow', 'Core Pilates Studio'],
            },
            {
                'full_name': 'Ivan Kuznetsov',
                'email': 'ivan@example.com',
                'courses': ['Power Strength Basics', 'HIIT Cardio Burn'],
            },
            {
                'full_name': 'Maria Volkova',
                'email': 'maria@example.com',
                'courses': ['Morning Yoga Flow', 'HIIT Cardio Burn'],
            },
        ]

        for item in member_data:
            member, _ = Member.objects.update_or_create(
                email=item['email'],
                defaults={
                    'full_name': item['full_name'],
                    'joined_date': today,
                },
            )
            member.courses.set(course_objects[title] for title in item['courses'])

        self.stdout.write(self.style.SUCCESS('Sample fitness catalog data created successfully.'))
