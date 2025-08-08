from django.urls import path
from .views import laptop, laptop_detail, laptop_edit, laptop_delete

urlpatterns = [
    path('', laptop, name='laptop'),  # List or create laptops
    path('laptop/<int:id>/', laptop_detail, name='laptop_detail'),  # Detail view
    path('laptop/edit/<int:id>/', laptop_edit, name='laptop_edit'),  # Edit view
    path('laptop/delete/<int:id>/', laptop_delete, name='laptop_delete'),  # Delete view
]