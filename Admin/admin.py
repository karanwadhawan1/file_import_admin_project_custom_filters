from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import City,User


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display=['city']

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display=['first_name','last_name','username','email','date_joined','city','age','gender']

