from django.shortcuts import render,redirect
from .models import Reservation
from .forms import ReserveForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

def new(request):
    form = ReserveForm()
    context = {
        'form': form
    }
    return render(request,'reservations/new.html',context)

def create(request):
    form = ReserveForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('reservations:index')