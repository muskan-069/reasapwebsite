from django.contrib import admin
from english.models import vocab
from english.models import parajum
from english.models import errordetect
from english.models import idioms
from english.models import sentence

class Authorvocab(admin.ModelAdmin):
    data=('Question','Option1','Option2','Option3','Option4','Corrans')

class Authorparajum(admin.ModelAdmin):
    data=('Ques','Op1','Op2','O3','Op4','Corans')

class Authorerrordetect(admin.ModelAdmin):
    data=('Ques1','Op11','Op12','Op13','Op14','Corans1')

class Authoridioms(admin.ModelAdmin):
    data=('Ques2','Op21','Op22','Op23','Op24','Corans2')

class Authorsentence(admin.ModelAdmin):
    data=('Ques3','Op31','Op32','Op33','Op34','Corans3')

admin.site.register(vocab, Authorvocab)
admin.site.register(parajum, Authorparajum)
admin.site.register(errordetect, Authorerrordetect)
admin.site.register(idioms, Authoridioms)
admin.site.register(sentence, Authorsentence)
# Register your models here.
