from django.contrib import admin
from .models import Vendor,Food
# Register your models here.
#python manage.py createsuperuser 創立root
#做註冊
admin.site.register(Vendor)
admin.site.register(Food)
