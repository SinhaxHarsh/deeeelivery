from django.contrib import admin
from .models import OrderModel,MenuItem,Category

admin.site.register(OrderModel)
admin.site.register(MenuItem)
admin.site.register(Category)