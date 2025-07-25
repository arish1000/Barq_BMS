from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Bank

@login_required
def bankView(request):
    banks = Bank.objects.all().values('id', 'name', 'is_islamic')
    return JsonResponse(list(banks), safe=False)