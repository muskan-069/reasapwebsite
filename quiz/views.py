from django.shortcuts import render
from quiz.models import Exam
from quiz.models import alphabetseries
from quiz.models import seatar
from quiz.models import ordrank
from quiz.models import bloodrel

def quiz1(request):
    exam = Exam.objects.all()
    return render(request,"quiz.html",{"exam":exam})
def alphaseries(request):
    exam1 = alphabetseries.objects.all()
    return render(request,"alphaseries.html",{"exam1":exam1})
def seatarr(request):
    exam2 = seatar.objects.all()
    return render(request,"seatAr.html",{"exam2":exam2})
def orderrank(request):
    exam3 = ordrank.objects.all()
    return render(request,"orderRank.html",{"exam3":exam3})
def bloodrelation(request):
    exam4 = bloodrel.objects.all()
    return render(request,"bldrel.html",{"exam4":exam4})
# Create your views here.
