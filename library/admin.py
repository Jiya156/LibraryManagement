from django.contrib import admin
from library.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","author","isbn","category","published_Year","availability")

admin.site.register(Book,BookAdmin)

# Register your models here.
