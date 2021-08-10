from .views import registration,customerlist,devicelist,reregister,service,CustomerAPIView,search
from django.urls import path,include



urlpatterns = [

    path('registration/',registration),
    path('customerlist/',customerlist),
    path('devicelist/',devicelist),
    path('reregister/<uuid>/',reregister),
    path('service/',service),
    path('search/',CustomerAPIView),
    path('searchh/',search),

]
