from django.shortcuts import render,redirect
from .forms import RestaurantCreateForm
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants':restaurants,
    }
    return render(request,'restaurants/index.html',context)

def detail(request,res_pk):
    restaurant = Restaurant.objects.get(pk=res_pk)
    context = {
        'restaurant': restaurant,
    }
    return render(request,'restaurants/detail.html',context)

def create_restaurants(request):
    if request.method == 'POST':
        create_form = RestaurantCreateForm(request.POST)
        if create_form.is_valid():
            restaurant = create_form.save()
            return redirect('restaurants:detail', restaurant.pk)
    else:
        create_form = RestaurantCreateForm()
    context = {
        'create_form':create_form,
    }
    return render(request,'restaurants/create_restaurants.html',context)