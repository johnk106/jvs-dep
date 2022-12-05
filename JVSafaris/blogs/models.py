from email.policy import default
from django.db import models

#table models
class BlogCategory(models.Model):
    category = models.CharField(max_length = 499)
    description = models.CharField(max_length = 400)

    def __str__(self):
        return self.category
class Author(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=5000)
    facebook = models.CharField(max_length=2000,default='',blank=True)
    twitter = models.CharField(max_length=2000,default='',blank=True)
    linkedin = models.CharField(max_length=2000,default='',blank=True)
    instagram = models.CharField(max_length=2000,default='',blank=True)
    youtube = models.CharField(max_length=2000,default='',blank=True)
    image = models.ImageField()

    def __str__(self):
        return str(self.name)

class Blog(models.Model):
    heading = models.CharField(max_length = 2000)
    image = models.FileField()
    category = models.ForeignKey(BlogCategory,on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self):
        return self.heading

class Subheading(models.Model):
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
    image = models.FileField()
    sub_heading = models.CharField(max_length = 400)

    def __str__(self):
        return self.sub_heading

class Paragraph(models.Model):
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
    heading = models.ForeignKey(Subheading,on_delete = models.CASCADE)
    content = models.CharField(max_length = 10000)
    

    def __str__(self):
        return self.content

class BlogComment(models.Model):
    name = models.CharField(max_length =255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=4000)
    blog = models.ForeignKey(Blog,on_delete = models.CASCADE)

    def __str__(self):
        return self.name



