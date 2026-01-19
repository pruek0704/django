from django.db import models

# Create your models here.
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, default= None, on_delete=models.CASCADE)
    
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    priority = models.CharField(
        max_length=10, 
        choices=PRIORITY_CHOICES, 
        default='medium'
    )