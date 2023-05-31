from django.db import models

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    datetime = models.DateTimeField()

    def __str__(self):
        return f'Transaction {self.id}'