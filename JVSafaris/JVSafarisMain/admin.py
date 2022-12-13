from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ServiceCategory)
admin.site.register(Service)
admin.site.register(ServiceItem)
admin.site.register(Package)
admin.site.register(PackageService)
admin.site.register(ServiceChargeCharter)
admin.site.register(ServiceItemGallery)
admin.site.register(Destination)
admin.site.register(Booking)
admin.site.register(Staff)
admin.site.register(Honeymoon)
admin.site.register(Testimonial)
admin.site.register(PackageCategory)
admin.site.register(PackageCharter)