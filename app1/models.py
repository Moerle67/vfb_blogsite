from django.db import models

# Create your models here.
class Kommentar(models.Model):
    ueberschrift = models.CharField(max_length=30, verbose_name="Überschrift")
    slug = models.CharField(max_length=30)
    kommentar = models.TextField()
    name = models.CharField(max_length=50, verbose_name="Nutzer, der wo eingetragen hat")
    email = models.CharField(max_length=50, verbose_name="E-Mail Adresse")
    def __str__(self):
        return f"{self.ueberschrift} / {self.name}"
    class Meta:
        verbose_name_plural = "Kommentare"