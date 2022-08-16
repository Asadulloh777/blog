from django.db import models

# Create your models here.
class Bolim(models.Model):
    nom = models.CharField(max_length=40)
    icon = models.CharField(max_length=40)
    def __str__(self):
        return self.nom

class Postlar(models.Model):
    bolimlar = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='media')
    matn = models.TextField()
    aftor = models.ImageField(upload_to='media')
    ism = models.CharField(max_length=40)
    sana = models.DateField(auto_now=True)
    vaqt = models.TimeField(auto_now=True)

class Sitelogo(models.Model):
    rasm_light = models.ImageField(upload_to='media')
    rasm_dark = models.ImageField(upload_to='media')

