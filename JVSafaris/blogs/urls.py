from django.urls import path
from . import views

app_name = 'JVSBlogs'
urlpatterns = [
        path('',views.index,name = 'index'),
        path('details/<int:id>',views.details,name = 'details'),
        path('blog-categories/<category>',views.category,name = 'category'),

        path('comment/<int:id>',views.comment,name = 'comment')

]