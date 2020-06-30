from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "PhoneSaleApp/index.html") 

def detail(request):
    return render(request, "PhoneSaleApp/ProductDetail.html") 