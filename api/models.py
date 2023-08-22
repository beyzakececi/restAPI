from django.db import models

class Dronlar(models.Model):
    marka = models.CharField(max_length=150, verbose_name="Marka")
    model = models.CharField(max_length=300, verbose_name="Model")
    urun_kodu = models.CharField(max_length=50, verbose_name="Ürün Kodu")
    fiyat = models.IntegerField(verbose_name="Fiyat")
    ozellikler = models.TextField(verbose_name="Özellikler")

    def str(self):
        return self.marka

    class Meta:
        verbose_name_plural = "Dronlar"
