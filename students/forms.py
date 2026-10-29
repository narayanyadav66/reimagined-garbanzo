
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'roll_number',
            'email',
            'age',
            'course',
            'marks',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),
            'roll_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 100
            }),
            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course'
            }),
            'marks': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 100,
                'step': '0.01'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        if not name:
            raise forms.ValidationError("Name cannot be empty.")

        return name

    def clean_roll_number(self):
        roll_number = self.cleaned_data['roll_number'].strip()

        if not roll_number:
            raise forms.ValidationError("Roll number cannot be empty.")

        return roll_number
