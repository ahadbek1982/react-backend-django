from customers.models import Customers
from customers.serializers import CustomersSerializers
from django.http import JsonResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        data = Customers.objects.all()
        serializer = CustomersSerializers(data, many=True)
        return Response({'customers': serializer.data})
    elif request.method == 'POST':
        serializer = CustomersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST', 'DELETE'])
def customer(request, id):
    try:

        data = Customers.objects.get(pk=id)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomersSerializers(data)
        return Response({'customer': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = CustomersSerializers(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
