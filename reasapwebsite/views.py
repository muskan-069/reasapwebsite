from django.shortcuts import render
from reasap.models import reasap1
from reasap.models import servicesec
from reasap.models import coursesec
from contact.models import contactEnquiry

def home(request):
    servcie_data = servicesec.objects.all()
    course_data = coursesec.objects.all()
    data1 = {
        'servcie_data': servcie_data,
        'course_data': course_data
    }
    return render(request, "template/index.html",data1)
def contact (request):
    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        en=contactEnquiry(name=name,email=email,message=message)
        en.save()
    return render(request, "index.html")


def about(request):
    return render(request, "about-us.html")
def reasoning(request):
    return render(request, "reasoning1.html")
def aptitude(request):
    return render(request, "aptitude1.html")
def english(request):
    return render(request, "verbal1.html")
def technical(request):
    return render(request, "technical1.html")




