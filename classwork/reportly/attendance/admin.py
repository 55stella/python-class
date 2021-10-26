from django.contrib import admin

# Register your models here.
from .models import Book
from .models import student
# admin.site.register(Book)
# admin.site.register(student)

@admin.register(Book)
class BookAdmin(admin. ModelAdmin):
    list_display=['title','no_of_pages','isbn','date']
    list_editable=['isbn']
    list_filter=['date']
    list_per_page=2
    