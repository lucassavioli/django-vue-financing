from rest_framework import serializers


class SacSerializer(serializers.Serializer):
    installments_number = serializers.IntegerField()
    installment = serializers.DecimalField(max_digits=10, decimal_places=2)
    interest = serializers.DecimalField(max_digits=10, decimal_places=2)
    amortization = serializers.DecimalField(max_digits=10, decimal_places=2)
    balance_due = serializers.DecimalField(max_digits=10, decimal_places=2)


class PriceSerializer(serializers.Serializer):
    installments_number = serializers.IntegerField()
    installment = serializers.DecimalField(max_digits=10, decimal_places=2)
    interest = serializers.DecimalField(max_digits=10, decimal_places=2)
    amortization = serializers.DecimalField(max_digits=10, decimal_places=2)
    balance_due = serializers.DecimalField(max_digits=10, decimal_places=2)
