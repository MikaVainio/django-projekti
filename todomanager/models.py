from django.db import models

class Kategoria(models.Model):
    nimi = models.CharField(max_length=100)

    def __str__(self):
        return self.nimi


class Tehtava(models.Model):
    otsikko = models.CharField(max_length=250)
    kuvaus = models.CharField(max_length=2000, default="", blank=True)
    tehty = models.BooleanField(default=False)
    kategoria = models.ForeignKey(
        Kategoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.otsikko
