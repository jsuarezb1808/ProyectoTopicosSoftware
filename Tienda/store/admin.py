from django.contrib import admin
from.models import gafas,bodega,Order
# Register your models here.

#this adds the tasks to the admin site in the project
admin.site.register(gafas)
admin.site.register(bodega)
admin.site.register(Order)
