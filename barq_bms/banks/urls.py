from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bank_list_view, name='bank_view'),
    path('<int:id>/', views.bank_detail_view, name='bank_detail_view'),
]




