from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.parse import urlencode


# Create your views here.
def index(request):
    page = request.GET.get('page')
    b = Paginator(Blog.objects.order_by('-id').all(),8)
    blogs = b.page(page)
    c = Paginator(BlogCategory.objects.all(),4)
    categories = c.page(1)
    recent = Paginator(Blog.objects.order_by('id').reverse(),4)
    recent_blogs = recent.page(1)
    return render(request,'blogs/blog-home.html',{'blogs':blogs,'categories':categories,'recent_blogs':recent_blogs})

def details(request,id):
    blog = Blog.objects.get(pk = id)
    c = Paginator(BlogCategory.objects.all(),5)
    categories = c.page(1)
    recent = Paginator(Blog.objects.order_by('id').reverse(),4)
    recent_blogs = recent.page(1)
    return render(request,'blogs/blog-detail.html',{'blog':blog,'categories':categories,'recent_blogs':recent_blogs})

def category(request,category):
    c = Paginator(BlogCategory.objects.all(),5)
    categories = c.page(1)
    recent = Paginator(Blog.objects.order_by('id').reverse(),4)
    recent_blogs = recent.page(1)
    cat = BlogCategory.objects.get(pk = category)
    blogs = Blog.objects.filter(category = cat.id).all()
    return render(request,'blogs/blog-home.html',{'blogs':blogs,'categories':categories,'recent_blogs':recent_blogs})

def comment(request,id):
    blog = Blog.objects.get(pk =id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        new_comment = BlogComment(name = name,email = email,phone = phone,message = message,blog = blog)
        new_comment.save()
        messages.success(request,'Your comment has saved succesfully')

      
        return HttpResponseRedirect(reverse('JVSBlogs:details',kwargs = {'id':int(id)}))

    else:
        pass


        
