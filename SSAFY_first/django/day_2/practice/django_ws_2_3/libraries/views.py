from django.shortcuts import render
from . import request_module

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    datas = request_module.result
    title_author = []
    for data in datas:
        title, author =data['제목'],data['저자']
        title_author.append((title,author))
    context = {
        'title_author':title_author
    }
    return render(request,'recommend.html',context)