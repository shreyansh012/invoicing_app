from django.urls import path
from . import views


urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('new/', views.invoice_create, name='invoice_create'),
    path('<int:pk>/edit/', views.invoice_edit, name='invoice_edit'),
    path('item/<int:pk>/', views.view_invoice_item, name='view_invoice_item'),
    path('item/<int:pk>/edit/', views.edit_invoice_item, name='edit_invoice_item'),
]   
