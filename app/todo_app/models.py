from django.db import models
import datetime

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=2000, default='')
    date_created = models.DateField(default=datetime.date.today)
    due_date = models.DateField(default=datetime.date.today)
    STATUS_CHOICES = [
        ('Done', 'Done'),
        ('Ongoing', 'Ongoing')
    ]
    status = models.CharField(max_length = 20, choices=STATUS_CHOICES, default = 'Done')
