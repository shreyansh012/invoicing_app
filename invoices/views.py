from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, InvoiceItem
from .forms import InvoiceForm, InvoiceItemForm, TaxForm

# Create your views here.


def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices})


def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == 'POST':
        item_form = InvoiceItemForm(request.POST)
        if item_form.is_valid():
            new_item = item_form.save(commit=False)
            new_item.invoice = invoice
            new_item.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        item_form = InvoiceItemForm()

    items_with_taxes = []
    for item in invoice.items.all():
        item_total_price = item.total_price()
        taxes = []
        for tax in item.taxes.all():
            calculated_tax = tax.calculate_tax(item_total_price)
            taxes.append({
                'title': tax.title,
                'rate': tax.rate,
                'calculated_tax': calculated_tax,
            })
        items_with_taxes.append({
            'id': item.id,
            'name': item.name,
            'price': item.price,
            'quantity': item.quantity,
            'total_price': item_total_price,
            'taxes': taxes,
        })

    context = {
        'invoice': invoice,
        'items_with_taxes': items_with_taxes,
        'subtotal': invoice.subtotal(),
        'total_taxes': invoice.total_taxes(),
        'total': invoice.total(),
        'item_form': item_form,
    }

    return render(request, 'invoices/invoice_detail.html', context)


def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm()
    return render(request, 'invoices/invoice_form.html', {'form': form})


def invoice_edit(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            invoice = form.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'invoices/invoice_form.html', {'form': form})


def view_invoice_item(request, pk):
    item = get_object_or_404(InvoiceItem, pk=pk)

    if request.method == 'POST':
        tax_form = TaxForm(request.POST)
        if tax_form.is_valid():
            new_tax = tax_form.save(commit=False)
            new_tax.item = item
            new_tax.save()
            return redirect('view_invoice_item', pk=item.pk)
    else:
        tax_form = TaxForm()

    taxes = []
    for tax in item.taxes.all():
        calculated_tax = tax.calculate_tax(item.total_price())
        taxes.append({
            'title': tax.title,
            'rate': tax.rate,
            'calculated_tax': calculated_tax,
        })
    context = {
        'item': item,
        'taxes': taxes,
        'tax_form': tax_form,
        'total_taxe': item.total_taxes(),
    }
    return render(request, 'invoices/view_invoice_item.html', context)


def edit_invoice_item(request, pk):
    item = get_object_or_404(InvoiceItem, pk=pk)
    if request.method == 'POST':
        form = InvoiceItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('view_invoice_item', pk=item.pk)
    else:
        form = InvoiceItemForm(instance=item)
    return render(request, 'invoices/edit_invoice_item.html', {'form': form, 'item': item, 'invoice': item.invoice, 'taxes': item.taxes.all()})
