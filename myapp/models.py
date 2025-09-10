from django.db import models

# Create your models here.
from django.db import models

class DataNegara(models.Model):
    nama_data = models.CharField(max_length=100)
    isi_data = models.TextField()

    def __str__(self):
        return self.nama_data
