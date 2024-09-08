from django import forms
from .models import Invoice, InvoiceItem, Tax


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['date', 'invoice_number', 'currency']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['name', 'price', 'quantity']


class TaxForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = ['title', 'rate']
