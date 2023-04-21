from django.contrib import admin
from quiz.models import Exam
from quiz.models import alphabetseries
from quiz.models import seatar
from quiz.models import ordrank
from quiz.models import bloodrel

class Authorquiz(admin.ModelAdmin):
    data=('Question','Option1','Option2','Option3','Option4','Corrans')

class Authoralphaseries(admin.ModelAdmin):
    data=('Ques','Op1','Op2','O3','Op4','Corans')

class Authorseatarrange(admin.ModelAdmin):
    data=('Ques1','Op11','Op12','Op13','Op14','Corans1')

class Authororderank(admin.ModelAdmin):
    data=('Ques2','Op21','Op22','Op23','Op24','Corans2')

class Authorbldrel(admin.ModelAdmin):
    data=('Ques3','Op31','Op32','Op33','Op34','Corans3')

admin.site.register(Exam, Authorquiz)
admin.site.register(alphabetseries, Authoralphaseries)
admin.site.register(seatar, Authorseatarrange)
admin.site.register(ordrank, Authororderank)
admin.site.register(bloodrel, Authorbldrel)
# Register your models here.
