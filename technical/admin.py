from django.contrib import admin
from technical.models import network
from technical.models import internet
from technical.models import cprog
from technical.models import c_prog
from technical.models import javaprog

class Authornetwork(admin.ModelAdmin):
    data=('Question','Option1','Option2','Option3','Option4','Corrans')

class Authorinternet(admin.ModelAdmin):
    data=('Ques','Op1','Op2','O3','Op4','Corans')

class Authorcprog(admin.ModelAdmin):
    data=('Ques1','Op11','Op12','Op13','Op14','Corans1')

class Authorc_prog(admin.ModelAdmin):
    data=('Ques2','Op21','Op22','Op23','Op24','Corans2')

class Authorjavaprog(admin.ModelAdmin):
    data=('Ques3','Op31','Op32','Op33','Op34','Corans3')

admin.site.register(network, Authornetwork)
admin.site.register(internet, Authorinternet)
admin.site.register(cprog, Authorcprog)
admin.site.register(javaprog, Authorjavaprog)
admin.site.register(c_prog, Authorc_prog)
# Register your models here.
