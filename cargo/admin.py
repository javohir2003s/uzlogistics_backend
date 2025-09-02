from django.contrib import admin
from .models import Cargo, Location, District, Region

# Register your models here.

admin.site.register(Cargo)
admin.site.register(Location)
admin.site.register(District)
admin.site.register(Region)
