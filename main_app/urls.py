  
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:item_id>', views.delete, name='delete'),
    path('add/', views.AddItem.as_view(), name="add"),
]