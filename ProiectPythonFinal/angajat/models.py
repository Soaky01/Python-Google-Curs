from django.db import models

# Create your models here.

class Angajat(models.Model):

    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    varsta = models.IntegerField(max_length=2)
    domeniu = models.CharField(max_length=100)
    salariu = models.IntegerField(max_length=10)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.nume} -> {self.prenume} -> {self.varsta} -> {self.domeniu} -> {self.salariu}"

class Log(models.Model):
    action_choices = (('created', 'created'),
                      ('updated', 'updated'),
                      ('refresh', 'refresh'))

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action = models.CharField(max_length=10, choices=action_choices)
    url = models.CharField(max_length=100)
