from rest_framework import serializers
from .models import Customer,Customerdetails,Devicedetails,Service


class CustomerSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customer
       fields='__all__'

class CustomerdetailsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customerdetails
       fields='__all__'

class DevicedetailsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Devicedetails
       fields='__all__'

class ServiceSerializer(serializers.ModelSerializer):
   class Meta:
       model = Service
       fields='__all__'