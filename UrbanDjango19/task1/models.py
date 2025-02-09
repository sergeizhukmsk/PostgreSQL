from django.db import models
from decimal import Decimal


class TypeValue(models.Model):
    id = models.AutoField(primary_key=True)  # Используйте AutoField для автоматической генерации id
    TypeValueName = models.CharField(max_length=50)
    TypeValueKind = models.CharField(max_length=10)
    ValCode = models.CharField(max_length=3)
    IsActive = models.SmallIntegerField()


    class Meta:
        db_table = '"public"."TypeValue"'
        constraints = [
            models.CheckConstraint(check=models.Q(IsActive__in=[0, 1]), name='is_active_check'),
        ]


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, through='Task1GameBuyer')

    def __str__(self):
        return self.title


class Task1GameBuyer(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
