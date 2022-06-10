from django.db import models


class Inventory(models.Model):
    name = models.CharField(max_length=254)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Inventory'
