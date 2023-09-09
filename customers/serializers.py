from rest_framework import serializers
from customers.models import Customers


class CustomersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"
