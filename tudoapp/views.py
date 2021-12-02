from django.shortcuts import render

# Create your views here.
from tudoapp.forms import toduModel


def fun(request):
    form=toduModel()
    return render(request,'home.html',{'form':form})

def update(request):
    return render(request,'update.html')