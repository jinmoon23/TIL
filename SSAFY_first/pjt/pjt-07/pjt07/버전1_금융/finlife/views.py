from django.shortcuts import render
import requests
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings
from .models import DepositProducts,DepositOptions
from .serializers import DepositProductSerializer,DepositOptionSerializer


BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'
# Create your views here.
@api_view(['GET'])
def index(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo':1,
    }
    response = requests.get(URL,params=params).json()
    return JsonResponse(response)

@api_view(['GET'])
def save_data(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo':1,
    }
    response = requests.get(URL,params=params).json()
    result = response.get('result')
    # 1. DepositProducts 모델의 필드에 값을 넣기 위해 찾기
    for base_list in result.get('baseList'):
        fin_prdt_cd = base_list.get('fin_prdt_cd')
        kor_co_nm = base_list.get('kor_co_nm')
        fin_prdt_nm = base_list.get('fin_prdt_nm')
        etc_note = base_list.get('etc_note')
        join_deny = base_list.get('join_deny')
        join_member = base_list.get('join_member')
        join_way = base_list.get('join_way')
        spcl_cnd = base_list.get('spcl_cnd')

        if DepositProducts.objects.filter(
            fin_prdt_cd=fin_prdt_cd,
            kor_co_nm=kor_co_nm,
            fin_prdt_nm=fin_prdt_nm,
            etc_note=etc_note,
            join_deny=join_deny,
            join_member=join_member,
            join_way=join_way,
            spcl_cnd=spcl_cnd,
        ).exists():
            continue
        else:
            data = {
                'fin_prdt_cd': fin_prdt_cd,
                'kor_co_nm': kor_co_nm,
                'fin_prdt_nm':fin_prdt_nm,
                'etc_note':etc_note,
                'join_member':join_member,
                'join_deny':join_deny,
                'join_way':join_way,
                'spcl_cnd':spcl_cnd,
            }
            serializer = DepositProductSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    for option_list in result.get('optionList'):
        # product = option_list.get('product')
        fin_prdt_cd = option_list.get('fin_prdt_cd')
        intr_rate_type_nm = option_list.get('intr_rate_type_nm')
        if option_list.get('intr_rate'):
            intr_rate = option_list.get('intr_rate')    
        else:
            intr_rate = -1
        if option_list.get('intr_rate2'):
            intr_rate2 = option_list.get('intr_rate2')    
        else:
            intr_rate2 = -1
        save_trm = option_list.get('save_trm')

        product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        data = {
            # 'product':product,
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm, 
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        serializer = DepositOptionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)
    return JsonResponse({
        'message':'저장 성공!'
    })            


@api_view(['GET'])
def deposit_products(request):
    products = DepositProducts.objects.all()
    serializer = DepositProductSerializer(products,many=True)
    return Response(serializer.data)

