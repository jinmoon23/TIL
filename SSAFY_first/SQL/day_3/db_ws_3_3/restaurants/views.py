from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm, MenuForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurants:detail', restaurant.pk)
    else:
        form = RestaurantForm()
    context = {
        'form': form
    }
    return render(request, 'restaurants/create.html', context)

def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    menu_form = MenuForm()
    context = {
        'restaurant': restaurant,
        'menu_form':menu_form,
    }
    return render(request, 'restaurants/detail.html', context)

def creates_menu(request,restaurant_pk):
    # 1. 어떤 restaurant(1)에 menu(N)들을 등록할거야?
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    # 2. 유저의 menu 등록이 적절했는지 확인해보자
    menu_form = MenuForm(request.POST)
    if menu_form.is_valid():
        # 3. 적절했어? 그럼 foreignKey 등록을 위해 객체 뽑자
        menu = menu_form.save(commit=False)
        # 4. foreignKey 등록 해주자
        menu.restaurant = restaurant
        # 5. 저자하자
        menu.save()
    return redirect('restaurants:detail', restaurant.pk)