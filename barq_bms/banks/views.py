from django.shortcuts import render
from django.http import HttpResponse

def bankView(request):
    return HttpResponse("Hello Banks!")