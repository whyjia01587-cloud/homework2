from django import forms

from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'category',
            'coach',
            'difficulty',
            'duration_minutes',
            'price',
            'start_date',
            'is_available',
            'image_url',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Morning Yoga Flow'}),
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe the training plan and goals.'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/course.jpg'}),
        }
        error_messages = {
            'title': {'required': 'Please enter the course title.'},
            'description': {'required': 'Please add a short course description.'},
            'category': {'required': 'Please choose a category.'},
            'coach': {'required': 'Please choose a coach.'},
            'duration_minutes': {'required': 'Please enter the duration in minutes.'},
            'price': {'required': 'Please enter the course price.'},
            'start_date': {'required': 'Please choose a start date.'},
        }

    def clean_duration_minutes(self):
        duration = self.cleaned_data['duration_minutes']
        if duration <= 0:
            raise forms.ValidationError('Duration must be greater than zero.')
        return duration

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Price cannot be negative.')
        return price
