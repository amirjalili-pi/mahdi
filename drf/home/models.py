from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.year}'


class Person(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
