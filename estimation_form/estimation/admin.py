from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Estimation,Shouhin,Print,Member


class A_estimation(ModelAdmin):
    model=Estimation
    list_display=["est_num","est_day","com","tantou","cus_com","cus_name"]


class A_shouhin(ModelAdmin):
    model=Shouhin
    list_display=["est_num","maker","shouhin_num","shouhin_name","color","size","suryo"]


class A_print(ModelAdmin):
    model=Print
    list_display=["est_num","point","color","way"]


class A_Member(ModelAdmin):
    model=Member
    list_display=["user_id","user_com"]


admin.site.register(Estimation,A_estimation)
admin.site.register(Shouhin,A_shouhin)
admin.site.register(Print,A_print)
admin.site.register(Member,A_Member)
