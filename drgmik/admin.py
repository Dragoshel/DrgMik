from django.contrib import admin

from .models import *

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Paragraph)
admin.site.register(Image)