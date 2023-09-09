from customers.models import Customers
from customers.serializers import CustomersSerializers
from django.http import HttpResponse


def customers(request):
    data = Customers.objects.all()
    serializer = CustomersSerializers(data, many=True)
    return HttpResponse({'customers': serializer.data})
