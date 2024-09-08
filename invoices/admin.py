from django.contrib import admin
from .models import Invoice, InvoiceItem, Tax

# Register your models here.


class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1


class TaxInline(admin.TabularInline):
    model = Tax
    extra = 1


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]


class InvoiceItemAdmin(admin.ModelAdmin):
    inlines = [TaxInline]


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(Tax)