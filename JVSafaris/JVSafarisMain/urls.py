from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'JVS'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('packages/',views.packages,name = 'packages'),
    path('packages/description/<package>',views.package_desc,name = 'package-desc'),
    path('services/',views.services_Categories,name = 'services'),
    path('about/',views.about,name = 'about'),
    path('testimonials/',views.testimonials,name = 'testimonials'),
    path('guides/',views.guide,name='guides'),
    path('contact/',views.contact,name = 'contact'),
    path('about/',views.about,name = 'about'),
    path('destinations/',views.destinations,name = 'destinations'),

    path('services/<int:id>',views.services,name = 'service-items'),
    path('package/booking/<int:id>',views.booking,name = 'booking'),
    path('package/booking/payment/<id>',views.payment,name = 'payments'),

    path('service/booking/<int:id>',views.service_booking,name = 'service-booking'  ),
    path('service/booking/payment/<int:id>',views.service_payment,name = 'service-payment'),



    path('auth/login/',views._login,name = 'login'),
    path('auth/sign-up/',views.sign_up,name = 'sign_up'),
    path('auth/logout/',views.logout_view,name = 'logout'),
    path('auth/login-required/',views.required,name = 'login-required'),


    path('service/details/<int:id>',views.service_details,name = 'service-detail')


]