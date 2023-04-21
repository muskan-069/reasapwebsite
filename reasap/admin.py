from django.contrib import admin
from reasap.models import reasap1
from reasap.models import servicesec
from reasap.models import coursesec
class AuthorReasap(admin.ModelAdmin):
    data=('name','mob')
class Authorservice(admin.ModelAdmin):
    data1=('head','content')
class Authorcourse(admin.ModelAdmin):
    data2 = ('top','sec1','sec2','sec3','sec4','sec5')
admin.site.register(reasap1, AuthorReasap)
admin.site.register(servicesec, Authorservice)
admin.site.register(coursesec, Authorcourse)
# Register your models here.
