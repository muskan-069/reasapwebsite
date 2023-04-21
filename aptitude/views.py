from django.shortcuts import render
from aptitude.models import SICI
from aptitude.models import LCMHCF
from aptitude.models import RatioP
from aptitude.models import TimeW
from aptitude.models import Simplication

def sc(request):
    data = SICI.objects.all()
    return render(request,"SI&CI.html",{"data":data})
def lchc(request):
    data1 = LCMHCF.objects.all()
    return render(request,"LCM&HCF.html",{"data1":data1})
def ratio(request):
    data2 = RatioP.objects.all()
    return render(request,"Ratio&Prop.html",{"data2":data2})
def time(request):
    data3 = TimeW.objects.all()
    return render(request,"Time&Work.html",{"data3":data3})
def simply(request):
    data4 = Simplication.objects.all()
    return render(request,"Simpli.html",{"data4":data4})
# Create your views here.
