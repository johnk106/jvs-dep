from email.policy import default
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=400)
    category_description = models.CharField(max_length=400)

    def __str__(self):
        return self.category_name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory,on_delete = models.CASCADE)
    category_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.category_description

class ServiceItem(models.Model):
    category = models.ForeignKey(ServiceCategory,on_delete= models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    item_description = models.CharField(max_length=400)
    optional = models.BooleanField()
    price = models.FloatField(default=0.0)
    desc = models.CharField(max_length=4000,default='')
    location = models.CharField(max_length=200,default='')
    image = models.FileField(default = '')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    duration = models.IntegerField(default=2)
    adults = models.IntegerField(default=2)
    kids = models.IntegerField(default=0)


    def __str__(self):
        return self.item_description


class ServiceItemGallery(models.Model):
    service_item = models.ForeignKey(ServiceItem,on_delete = models.CASCADE)
    image = models.FileField(default = '')

class Destination(models.Model):
    destinantion_name = models.CharField(max_length = 400)
    image = models.FileField(default = '')

    def __str__(self):
        return self.destinantion_name
   

class ServiceChargeCharter(models.Model):
    category = models.ForeignKey(ServiceCategory,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    service_item = models.ForeignKey(ServiceItem,on_delete=models.CASCADE)
    service_charger = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class PackageCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1200)

    def __str__(self):
        return self.name


class Package(models.Model):
    package_name = models.CharField(max_length=400)
    start_date = models.DateField()
    end_date = models.DateField()
    package_desc = models.CharField(max_length=1000)
    image = models.FileField(default = '')
    destination = models.ForeignKey(Destination,on_delete = models.CASCADE,default = 1)
    duration = models.IntegerField(default = 2)
    population = models.IntegerField(default = 2)
    kids = models.IntegerField(default=0)
    category = models.ForeignKey(PackageCategory,on_delete=models.CASCADE)


    def __str__(self):
        return self.package_name

class PackageService(models.Model):
    service = models.CharField(max_length = 255)
    package = models.ForeignKey(Package,on_delete = models.CASCADE,default = '')
    is_optional = models.BooleanField(default = True)
    price = models.FloatField(default = 0.0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.service


class Booking(models.Model):
    fname = models.CharField(max_length = 255)
    lname = models.CharField(max_length = 255)
    adults = models.IntegerField()
    kids = models.IntegerField()
    country = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 200)
    package = models.ForeignKey(Package,on_delete = models.CASCADE)
    amount = models.FloatField()
    isPaid = models.BooleanField(default = False)

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)


class ServiceBooking(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length = 255)
    adults = models.IntegerField()
    kids = models.IntegerField()
    country = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 200)
    service = models.ForeignKey(ServiceItem,on_delete = models.CASCADE)
    amount = models.FloatField()
    isPaid = models.BooleanField(default = False)

    def __str__(self):
        return str(self.fname) + ' ' + str(self.lname)

class Staff(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField()
    twitter = models.CharField(max_length = 1000,blank = True)
    facebook = models.CharField(max_length = 1000,blank=True)
    instagram = models.CharField(max_length = 1000,blank=True)
    linkedin = models.CharField(max_length = 1000,blank = True)
    isEstemeed = models.BooleanField()

    def __str__(self):
        return str(self.name)

class Honeymoon(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    destination = models.ForeignKey(Destination,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=4200)
    message = models.CharField(max_length=4200)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Testimonial(models.Model):
    name = models.CharField(max_length = 255)
    comment = models.CharField(max_length=1200)
    occupation = models.CharField(max_length = 255)
    image = models.ImageField()

    def __str__(self):
        return self.name

