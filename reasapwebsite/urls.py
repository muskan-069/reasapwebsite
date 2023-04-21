"""reasapwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reasapwebsite import views
from quiz.views import *
from aptitude.views import *
from english.views import *
from technical.views import *
from django.conf import settings
from django.conf.urls.static import static
from auth_system.views import Login
from auth_system.views import Register
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name ="homepage"),
    path('about-us/',views.about, name ="aboutpage"),
   path('contact/', views.contact, name="contactsec"),
    path('reasoning/',views.reasoning, name="reasoningpage"),
    path('aptitude/',views.aptitude, name="aptitudepage"),
    path('english/',views.english, name="englishpage"),
    path('technical/',views.technical, name="technicalpage"),
    path('cod_decode/',quiz1, name='code-decode-page'),
    path('alphabetseries/',alphaseries, name="alphabetseriespage"),
    path('seatarrange/',seatarr, name="seatingpage"),
    path('order&ranking/',orderrank, name="orderrankpage"),
    path('bloodRelation/',bloodrelation, name="bloodrelationpage"),
    path('SI&CI/',sc, name="SICIpage"),
    path('LCM&HCF/',lchc, name="lchcpage"),
    path('Ratio&Proportion/',ratio, name="rppage"),
    path('Time&Work/',time, name="twpage"),
    path('Simplification/',simply, name="simpage"),
     path('vocab/',vocabulary, name="vocabpage"),
    path('parajumbles/',parajumbles, name="parajumbpage"),
    path('errordetection/',error, name="errorpage"),
    path('idioms/',idiom, name="idiompage"),
    path('sentencecompletion/',sentcom, name="sentencepage"),
    path('network/',net, name="netwrokpage"),
    path('internet/',internetwork, name="internetpage"),
    path('cprog/',cprogramming, name="cprogpage"),
    path('c++prog/',c_programming, name="c++progpage"),
    path('javaprog/',javaprogramming, name="javaprogpage"),
    path('register/',Register,name="register"),
    path('login/',Login,name="login-page"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
