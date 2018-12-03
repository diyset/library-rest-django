from django.contrib import admin
from .models import Book, Member, Order, BookCategory

# Register your models here.
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Order)
admin.site.register(BookCategory)
