from django.shortcuts import render
from english.models import vocab
from english.models import parajum
from english.models import errordetect
from english.models import idioms
from english.models import sentence

def vocabulary(request):
    data = vocab.objects.all()
    return render(request,"vocab.html",{"data":data})
def parajumbles(request):
    data1 = parajum.objects.all()
    return render(request,"parajumb.html",{"data1":data1})
def error(request):
    data2 = errordetect.objects.all()
    return render(request,"errordetect.html",{"data2":data2})
def idiom(request):
    data3 = idioms.objects.all()
    return render(request,"idioms.html",{"data3":data3})
def sentcom(request):
    data4 = sentence.objects.all()
    return render(request,"sentence.html",{"data4":data4})
# Create your views here.
