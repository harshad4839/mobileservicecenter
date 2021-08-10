from django.db import models
import uuid

#from versatileimagefield.fields import VersatileImageField

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    mobileno=models.CharField(max_length=10, null=True, blank=True)
    complaint = models.CharField(max_length=100, null=True, blank=True)
    modelname = models.CharField(max_length=100, null=True, blank=True)
    modelbrand = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    images = models.ImageField('images',null=True)
    #image = VersatileImageField('image',null=True )


    def __str__(self):
        return self.name


class Customerdetails(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=100)
    email =models.EmailField(max_length=100)


    def __str__(self):
        return self.name

class Devicedetails(models.Model):
    modelbrand = models.CharField(max_length=100, null=True, blank=True)
    modelname = models.CharField(max_length=100, null=True, blank=True)
    modelno = models.CharField(max_length=100, null=True, blank=True)
    imeino=models.CharField(max_length=16,null=True, blank=True)
    colour=models.CharField(max_length=20,null=True,blank=True)


    def __str__(self):
        return self.modelbrand

class Service(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    mobileno = models.CharField(max_length=10, null=False, blank=True)
    complaint = models.CharField(max_length=100, null=True, blank=True)
    modelname = models.CharField(max_length=100, null=True, blank=True)
    modelbrand = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    images = models.ImageField('images', null=True)
    payment=models.IntegerField(null=True)

    status_onprogress = (
        ("completed", "completed"),
        ("deliverd", "deliverd"),
        ("recived", "recived"),
        ("working", "working"),
    )
    status = models.CharField(
        max_length=20,
        choices=status_onprogress,
        default='working'
    )
    payment = models.IntegerField(null=True)
    expected_delivery=models.DateTimeField(null=True,blank=True)
    actual_delivery = models.DateTimeField(null=True, blank=True)


    class Meta:
        ordering = ['-created', 'uuid']