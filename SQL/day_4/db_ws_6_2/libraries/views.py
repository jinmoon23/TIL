from django.shortcuts import render

# Create your views here.
def root(request):
    return render(request,'libraries/root.html')