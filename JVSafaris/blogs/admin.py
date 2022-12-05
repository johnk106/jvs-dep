from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(Subheading)
admin.site.register(Paragraph)
admin.site.register(BlogComment)
admin.site.register(Author)