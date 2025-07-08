from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Bank

def bankView(request):
    banks = Bank.objects.all().values('id', 'name', 'is_islamic')
    return JsonResponse(list(banks), safe=False)