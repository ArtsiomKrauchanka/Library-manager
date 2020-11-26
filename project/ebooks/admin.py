from django.contrib import admin
from .models import Ebook
# Register your models here.

@admin.register(Ebook)
class OpinionAdmin(admin.ModelAdmin):
    search_fields = ('book__title', 'book__author__first_name', 'book__author__last_name')