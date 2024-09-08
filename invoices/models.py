from django.db import models

# Create your models here.


class Invoice(models.Model):
    date = models.DateField()
    invoice_number = models.CharField(max_length=20, unique=True)
    currency = models.CharField(max_length=3)

    def subtotal(self):
        return sum(item.total_price() for item in self.items.all())

    def total_taxes(self):
        return sum(item.total_taxes() for item in self.items.all())

    def total(self):
        return self.subtotal() + self.total_taxes()


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def total_price(self):
        return self.price * self.quantity

    def total_taxes(self):
        return sum(tax.calculate_tax(self.total_price()) for tax in self.taxes.all())
    

class Tax(models.Model):
    item = models.ForeignKey(InvoiceItem, related_name='taxes', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def calculate_tax(self, price):
        return (self.rate / 100) * price
