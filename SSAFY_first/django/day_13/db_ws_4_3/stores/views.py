from django.shortcuts import render,redirect
from .models import Store
from .forms import StoreCreateForm, ProductCreateForm
# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    product_create_form = ProductCreateForm()
    context = {
        'store': store,
        'product_create_form':product_create_form,
    }
    return render(request, 'stores/detail.html', context)

def creates_store(request):
    # 2. form을 건네받은 경우
    if request.method == 'POST':
        # 3. 신규 매장 정보를 변수에 담고
        create_form = StoreCreateForm(request.POST)
        # 4. 그 정보가 담긴 폼을 점검하고
        if create_form.is_valid():
            store = create_form.save()
            return redirect('stores:detail', store.pk)
    else:
        # 1. 건네줄 form을 변수에 담자
        create_form = StoreCreateForm()
    context = {
        'create_form': create_form,
    }
    return render(request,'stores/create_store.html',context)

def creates_product(request,store_pk):
    # 1. 물건을 추가하려는 매장이 어떤 매장인지 식별하자
    store = Store.objects.get(pk=store_pk)
    # 2. 사용자가 입력한 물건의 입력값을 받아오자
    product_create_form = ProductCreateForm(request.POST)
    # 3. 잘 입력했니?
    if product_create_form.is_valid():
        # 4. foreignKey가 2개나 있어
        product = product_create_form.save(commit=False)
        # 5. user부터 등록하자
        product.user = request.user
        # 6. store 등록하자
        product.store = store
        # 7. 최종 저장하자
        product.save()
    return redirect('stores:detail',store.pk)