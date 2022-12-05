from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Booking, Destination, Package, ServiceBooking, ServiceCategory, ServiceItem
from django.core.paginator import Paginator
from blogs.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    destinations = Destination.objects.all()

    p = Paginator(Package.objects.order_by('id').all(),6)
    packages = p.page(1)

    b = Paginator(Blog.objects.order_by('id').all(),3)
    blogs = b.page(1)

    return render(request,'JVSafarisMain/index.html',{
        'destinations':destinations,
        'packages':packages,
        'blogs':blogs
    })


def packages(request):
    packages = Package.objects.all()
    destinations = Destination.objects.all()
    return render(request,'JVSafarisMain/package.html',{'packages':packages,'destinations':destinations})

def package_desc(request,package):
    _package = Package.objects.get(pk = package)
    return render(request,'JVSafarisMain/package-detail.html',{'package':_package})


def about(request):
    return render(request,'JVSafarisMain/about.html',{})

def services_Categories(request):
    services = ServiceCategory.objects.all()
    return render(request,'JVSafarisMain/service.html',{'services':services})

def services(request,id):
    service = ServiceCategory.objects.get(pk = id)
    return render(request,'JVSafarisMain/service-categories.html',{'service':service})

def testimonials(request):
    return render(request,'JVSafarisMain/testimonial.html',{})



def contact(request):
    return render(request,'JVSafarisMain/contact.html',{})

def destinations(request):
    destinations = Destination.objects.all()
    return render(request,'JVSafarisMain/destination.html',{'destinations':destinations})

def guide(request):
    return render(request,'JVSafarisMain/guide.html',{})


def _login(request):
    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(request, username=email, password=password)
    if user is not None:
        login(request,user)
        messages.success(request,'Welcome back {0},we are happy to see you again.'.format(user.first_name))
        return HttpResponseRedirect(reverse('JVS:index'))
    else:
        messages.warning(request,'Wrong credential combination,please check your credentials and try again.')
        return HttpResponseRedirect(reverse('JVS:index'))


def sign_up(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    password = request.POST['password']
    cpass = request.POST['cpassword']

    if password == cpass:
        try:
            user = User.objects.create_user(first_name = fname, last_name = lname, email = email,password = password,username=email)
            user.save()
            login(request,user)
            messages.success(request,'Congratulations {0},You have been successfully registered'.format(fname))
            return HttpResponseRedirect(reverse('JVS:index'))
        except:
            messages.warning(request,'That username is already taken,please choose another name.')
            return HttpResponseRedirect(reverse('JVS:index'))
    else:
        messages.warning(request,'Passwords do not match,sign up failed')
        return HttpResponseRedirect(reverse('JVS:index'))
        
@login_required(login_url='JVS:login-required')
def logout_view(request):
    logout(request)
    messages.warning(request,'You have been successfully logged out.')
    return HttpResponseRedirect(reverse('JVS:index'))

def required(request):
    messages.warning(request,'Please log in to access this feature')
    return HttpResponseRedirect(reverse('JVS:index'))


def service_details(request,id):
    service = ServiceItem.objects.get(pk = id)

    return render(request,'JVSafarisMain/service detail.html',{'service':service})


def booking(request,id):
    package = Package.objects.get(pk = id)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        adults  = request.POST['adults']
        kids = request.POST['kids']
        country = request.POST['country']
        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']

        amount = 100


        new_booking = Booking(fname = fname,lname = lname,adults = adults,kids = kids,country = country,city = city,email = email,phone = phone,package = package,amount = amount)
        new_booking.save()
        messages.success(request,'Your booking is saved successfully kindly make payments and reserve.')
        #return HttpResponseRedirect(reverse('JVS:payment'))
        return redirect('JVS:payments',id = new_booking.id)

    return render(request,'JVSafarisMain/booking.html',{'package':package})

def payment(request,id):
    booking = Booking.objects.get(pk = id)
    return render(request,'JVSafarisMain/payment.html',{'booking':booking})



def service_booking(request,id):
    service = ServiceItem.objects.get(pk = id)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        adults  = request.POST['adults']
        kids = request.POST['kids']
        country = request.POST['country']
        city = request.POST['city']
        email = request.POST['email']
        phone = request.POST['phone']
        amount = 100

        new_booking = ServiceBooking(fname = fname,lname = lname,adults = adults,kids = kids,country = country,city = city,email = email,phone = phone,service = service,amount = amount)
        new_booking.save()

        messages.success(request,'Your booking is saved successfully kindly make payments and reserve.')
        #return HttpResponseRedirect(reverse('JVS:payment'))
        return redirect('JVS:service-payment',id = new_booking.id)
    return render(request,'JVSafarisMain/service-booking.html',{'service':service})

def service_payment(request,id):
    booking = ServiceBooking.objects.get(pk = id)
    return render(request,'JVSafarisMain/service-payment.html',{'booking':booking})