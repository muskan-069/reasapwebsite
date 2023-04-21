from django.contrib import admin
from aptitude.models import SICI
from aptitude.models import LCMHCF
from aptitude.models import RatioP
from aptitude.models import TimeW
from aptitude.models import Simplication

class AuthorSICI(admin.ModelAdmin):
    data=('Question','Option1','Option2','Option3','Option4','Corrans')

class AuthorLCMHCF(admin.ModelAdmin):
    data1=('Ques','Op1','Op2','O3','Op4','Corans')

class AuthorRatioP(admin.ModelAdmin):
    data2=('Ques1','Op11','Op12','Op13','Op14','Corans1')

class AuthorTimeW(admin.ModelAdmin):
    data3=('Ques2','Op21','Op22','Op23','Op24','Corans2')

class AuthorSimplication(admin.ModelAdmin):
    data4=('Ques3','Op31','Op32','Op33','Op34','Corans3')

admin.site.register(SICI, AuthorSICI)
admin.site.register(LCMHCF, AuthorLCMHCF)
admin.site.register(RatioP, AuthorRatioP)
admin.site.register(TimeW, AuthorTimeW)
admin.site.register(Simplication, AuthorSimplication)
# Register your models here.
