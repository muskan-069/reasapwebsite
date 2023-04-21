from django.shortcuts import render
from technical.models import network
from technical.models import internet
from technical.models import cprog
from technical.models import c_prog
from technical.models import javaprog

def net(request):
    data = network.objects.all()
    return render(request,"networking.html",{"data":data})
def internetwork(request):
    data1 = internet.objects.all()
    return render(request,"internet.html",{"data1":data1})
def cprogramming(request):
    data2 = cprog.objects.all()
    return render(request,"Cprog.html",{"data2":data2})
def javaprogramming(request):
    data3 = javaprog.objects.all()
    return render(request,"javaProg.html",{"data3":data3})
def c_programming(request):
    data4 = c_prog.objects.all()
    return render(request,"C++prog.html",{"data4":data4})
# Create your views here.
