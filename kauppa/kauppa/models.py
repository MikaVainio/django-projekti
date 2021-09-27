from django.db import models


class Tuote(models.Model):
    nimi = models.CharField(max_length=100)
    hinta = models.DecimalField(max_digits=9, decimal_places=2)  # 1 234 567.89

    def __str__(self):
        return f"Tuote: {self.nimi}"
