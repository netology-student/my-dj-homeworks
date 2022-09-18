from django.contrib import admin
from phones.models import Phone

# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','price','release_date','lte_exists']