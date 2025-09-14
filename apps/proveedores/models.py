from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.nombre} {self.razon_social} {self.cuit}"
    

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"