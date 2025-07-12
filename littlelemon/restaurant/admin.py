from django.contrib import admin
from .models import Booking, Menu
from rest_framework.authtoken.models import Token

admin.site.register(Token)
admin.site.register(Booking)
admin.site.register(Menu)   
# Register your models here.
