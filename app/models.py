from django.db import models

# Create your models here.

class State(models.Model):
    id=models.PositiveIntegerField()
    s=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.s

class Cap(models.Model):
    s=models.OneToOneField(State,on_delete=models.CASCADE)
    c=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.c