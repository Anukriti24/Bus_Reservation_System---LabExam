from django.shortcuts import render

from .models import BookingListItem 
from django.http import HttpResponseRedirect 

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login')
def bookingappView(request):
    
    user_email = request.user.email
    
    all_booking_items = BookingListItem.objects.filter(user=user_email)
    return render(request, 'reservation.html',  {'all_booking':all_booking_items})


@login_required(login_url='/login')
def addBooking(request):
    # x = request.POST.get('todotext')
    user_email = request.user.email
    new_item = BookingListItem()
    new_item.user = user_email
    new_item.content = request.POST.get('content')
    new_item.save()
    return HttpResponseRedirect('/book/') 

@login_required(login_url='/login')
def deleteBooking(request, i):
    y = BookingListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/book/') 