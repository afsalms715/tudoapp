from django.shortcuts import render, redirect

# Create your views here.
from tudoapp.forms import toduModel
from tudoapp.models import tudo


def fun(request):
    form=toduModel()
    todus=tudo.objects.all()
    if request.method == 'POST':
        form=toduModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'home.html',{'form':form,'todus':todus})

def update(request,todu_id):
    tudoss=tudo.objects.get(id=todu_id)
    form = toduModel(instance=tudoss)
    if request.method == 'POST':
        form=toduModel(request.POST,instance=tudoss)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'update.html',{'form':form})

def delete(request,todu_id):
    if request.method == 'POST':
        tudo.objects.get(id=todu_id).delete()
        return redirect('home')