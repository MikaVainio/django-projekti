from django.db import models

class Tehtava(models.Model):
    otsikko = models.CharField(max_length=250)
    kuvaus = models.CharField(max_length=2000, default="", blank=True)

    def __str__(self):
        return self.otsikko
