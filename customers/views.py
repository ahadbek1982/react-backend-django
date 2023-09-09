from customers.models import Customers
from customers.serializers import CustomersSerializers
from django.http import JsonResponse


def customers(request):
    data = Customers.objects.all()
    serializer = CustomersSerializers(data, many=True)
    return JsonResponse({'customers': serializer.data})


def customer(request, id):
    data = Customers.objects.get(pk=id)
    serializer = CustomersSerializers(data)
    return JsonResponse({'customer': serializer.data})
