
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )
    course = models.CharField(max_length=100)
    marks = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"

    class Meta:
        ordering = ['name']
