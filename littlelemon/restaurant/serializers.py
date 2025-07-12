from rest_framework import serializers
from .models import Menu,Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'  # or list specific fields like ['Title', 'Price', 'Inventory']
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'  # or list specific fields like ['Title', 'Price', 'Inventory']