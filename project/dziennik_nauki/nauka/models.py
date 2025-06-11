from django.db import models
from django.contrib.auth.models import User

POZIOMY = [
    ('P', 'Początkujący'),
    ('Ś', 'Średniozaawansowany'),
    ('Z', 'Zaawansowany'),
]

class Temat(models.Model):
    nazwa = models.CharField(max_length=100)
    poziom = models.CharField(max_length=1, choices=POZIOMY)
    osiagniecia = models.TextField()
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa

class Notatka(models.Model):
    temat = models.ForeignKey(Temat, on_delete=models.CASCADE)
    tresc = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notatka do: {self.temat.nazwa} ({self.data.date()})"
