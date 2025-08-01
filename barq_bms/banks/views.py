from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Bank
from .serializers import BankSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bank_list_view(request):
    banks = Bank.objects.all().values('id', 'name', 'is_islamic')
    return Response(list(banks))

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bank_detail_view(request, id):
    try:
        bank = Bank.objects.get(pk=id)
        serializer = BankSerializer(bank)
        return Response(serializer.data)
    except Bank.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)