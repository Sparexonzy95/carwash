from django.contrib import admin
from .models import CarWash
# Register your models here.


@admin.register(CarWash)
class CarwashAdmin(admin.ModelAdmin):
    list_display = CarWash.DisplayFields
    search_fields =  SearchableFields =['Customer__username','plate_number','subcription_packages',]
    list_filter = CarWash.FilterFields