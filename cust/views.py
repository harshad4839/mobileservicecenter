from django.shortcuts import render
from rest_framework import generics

#from django_filters import FilterSet
#from  django_filters import filters

from rest_framework import filters
from django.http import HttpResponse, JsonResponse

from .models import Customer, Customerdetails, Devicedetails, Service
from .serializers import CustomerSerializer, CustomerdetailsSerializer, DevicedetailsSerializer, ServiceSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def registration(request):
    if request.method == 'GET':
        Customers = Customer.objects.all()
        serializer = CustomerSerializer(Customers, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def reregister(request, uuid):
    try:
        customers = Customer.objects.get(uuid=uuid)

    except Customer.DoesnotExist:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CustomerSerializer(customers)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customers.delete()
        customers.active_status = False
        customers.save
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customerlist(request):
    if request.method == 'GET':
        Customerdetailss = Customerdetails.objects.all()
        serializer = CustomerdetailsSerializer(Customerdetailss, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = CustomerdetailsSerailizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def devicelist(request):
    if request.method == 'GET':
        Devicedetailss = Devicedetails.objects.all()
        serializer = DevicedetailsSerializer(Devicedetailss, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = DevicedetailsSerailizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def service(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerAPIView(generics.ListCreateAPIView):
    search_fields = ['mobileno']
    print(search_fields)
    filter_backends = (filters.SearchFilter,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@api_view(['GET'])
def search(request):
    key = request.GET['key']
    data = Customer.objects.filter(mobileno__istartswith=key)
    serializer = CustomerSerializer(data, many=True)
    return Response(serializer.data)

