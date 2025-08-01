from rest_framework import serializers
from banks.models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = [
            'id',
            'name',
        ]

