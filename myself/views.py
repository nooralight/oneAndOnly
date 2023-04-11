from django.shortcuts import render

# Create your views here.

#Goto index

def gotoHome(request):
    return render(request,"index.html")