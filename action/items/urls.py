from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('items/', views.items, name='items'),
    path('add/', views.add_item, name='add'),
    path('<uuid:pk>/', views.view_items, name='view'),
    path('<uuid:pk>/edit/', views.edit_items, name='edit'),
    path('<uuid:pk>/delete/', views.delete_items, name='delete'),
] 