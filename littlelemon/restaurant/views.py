from django.shortcuts import render
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView,DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def index(request):
	return render(request, 'index.html', {})
# Create your views here.
class MenuItemView(ListAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

class SingleMenuItemView(RetrieveAPIView,DestroyAPIView):
	permission_classes = [IsAuthenticated]
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

class BookingViewSet(ModelViewSet):
	permission_classes = [IsAuthenticated]
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

	