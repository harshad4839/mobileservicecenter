
from django.contrib import admin
from .models import Customer
from .models import Customerdetails
from .models import Devicedetails
from .models import Service


admin.site.register(Customer)
admin.site.register(Customerdetails)
admin.site.register(Devicedetails)
admin.site.register(Service)

