from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(120)])

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=150)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Renters (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    data = models.DateField()  # Или другой подходящий тип данных
    period_of_renting = models.IntegerField()  # Или другой подходящий тип данных

