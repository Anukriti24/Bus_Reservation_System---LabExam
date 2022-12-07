from django.urls import path
# from django.urls import path, include
from . import views
 
app_name = 'Booking_App'
urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('book/',views.bookingappView, name='book'),
    path('addBooking/',views.addBooking), 
    path('deleteBooking/<int:i>/', views.deleteBooking),
]
