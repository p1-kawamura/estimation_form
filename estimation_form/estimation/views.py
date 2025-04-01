from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
import datetime
from django.http import JsonResponse
import json
from .models import Estimation,Shouhin,Print,Member
from django.db.models import Max


@login_required
def index(request):
    if "form" not in request.session:
        request.session["form"]={}
    if "shouhin" not in request.session:
        request.session["shouhin"]=[]
    if "print" not in request.session:
        request.session["print"]=[]
    if "design_yes" not in request.session:
        request.session["design_yes"]=[False,False,False,False,False]

    shouhin_li=request.session["shouhin"]
    for i,h in enumerate(shouhin_li):
        ans=0
        for j in h["size_li"]:
            if j !="":
                ans+=int(j)
        h["index"]=i
        h["sum"]=ans

    print_li=request.session["print"]
    for i,h in enumerate(print_li):
        h["index"]=i

    size_li=["XXS","XS","S","M","L","LL","3L","4L"]

    design_yes=request.session["design_yes"]
    design_type=["イラストレータ（.ai）","フォトショップ（.psd）","画像データ（.jpg / .tiff / .pdf）","手書きデータ","その他（右の備考欄にご記入ください）"]
    design_li={}
    for i in range(len(design_type)):
        design_li[design_type[i]]=design_yes[i]

    user_id=request.user.username
    user_com=Member.objects.get(user_id=user_id).user_com
    form_li=request.session["form"]
    if len(form_li)==0:
        form_li["f_com"]=user_com

    params={
        "size_li":size_li,
        "form_li":form_li,
        "shouhin_li":shouhin_li,
        "print_li":request.session["print"],
        "design_li":design_li,
        "user_id":user_id,
    }

    return render(request,"estimation/index.html",params)


# 商品_追加_修正
def shouhin_add_up(request):
    add_up_num=request.POST.get("add_up_num")
    maker=request.POST.get("maker")
    shouhin_num=request.POST.get("shouhin_num")
    shouhin_name=request.POST.get("shouhin_name")
    color=request.POST.get("color")
    new_size_1=request.POST.get("new_size_1")
    new_size_2=request.POST.get("new_size_2")
    size_li=request.POST.get("size_li")
    size_li=json.loads(size_li)
    form_li=request.POST.get("form_li")  
    form_li=json.loads(form_li)
    design_yes=request.POST.get("design_yes")  
    design_yes=json.loads(design_yes)

    shouhin=request.session["shouhin"]
    if add_up_num=="add":
        dic={
            "maker":maker,
            "shouhin_num":shouhin_num,
            "shouhin_name":shouhin_name,
            "color":color,
            "new_size_1":new_size_1,
            "new_size_2":new_size_2,
            "size_li":size_li
        }
        shouhin.append(dic)
    else:
        i=int(add_up_num)
        shouhin[i]["maker"]=maker
        shouhin[i]["shouhin_num"]=shouhin_num
        shouhin[i]["shouhin_name"]=shouhin_name
        shouhin[i]["color"]=color
        shouhin[i]["new_size_1"]=new_size_1
        shouhin[i]["new_size_2"]=new_size_2
        shouhin[i]["size_li"]=size_li

    request.session["form"]=form_li
    request.session["shouhin"]=shouhin
    request.session["design_yes"]=design_yes

    d={}
    return JsonResponse(d)


# 商品_編集（モーダルへの情報）
def shouhin_modal_up(request):
    index=int(request.POST.get("index"))
    shouhin=request.session["shouhin"]
    d={"shouhin":shouhin[index]}
    return JsonResponse(d)


# 商品_削除
def shouhin_del(request):
    index=int(request.POST.get("index"))
    form_li=request.POST.get("form_li")  
    form_li=json.loads(form_li)
    design_yes=request.POST.get("design_yes")  
    design_yes=json.loads(design_yes)

    shouhin=request.session["shouhin"]
    del shouhin[index]

    request.session["shouhin"]=shouhin
    request.session["form"]=form_li
    request.session["design_yes"]=design_yes
    d={}
    return JsonResponse(d)


# プリント_追加_修正
def print_add_up(request):
    add_up_num=request.POST.get("add_up_num")
    form_li=request.POST.get("form_li")  
    form_li=json.loads(form_li)
    design_yes=request.POST.get("design_yes")  
    design_yes=json.loads(design_yes)
    point=request.POST.get("point")
    color=request.POST.get("color")
    way=request.POST.get("way")

    print_li=request.session["print"]
    if add_up_num=="add":
        dic={"point":point,"color":color,"way":way}
        print_li.append(dic)
    else:
        i=int(add_up_num)
        print_li[i]["color"]=color
        print_li[i]["way"]=way

    request.session["print"]=print_li
    request.session["form"]=form_li
    request.session["design_yes"]=design_yes
    d={}
    return JsonResponse(d)


# プリント_編集（モーダルへの情報）
def print_modal_up(request):
    index=int(request.POST.get("index"))
    print_li=request.session["print"]
    d={"print":print_li[index]}
    return JsonResponse(d)


# プリント_削除
def print_del(request):
    index=int(request.POST.get("index"))
    form_li=request.POST.get("form_li")  
    form_li=json.loads(form_li)
    design_yes=request.POST.get("design_yes")  
    design_yes=json.loads(design_yes)

    print_li=request.session["print"]
    del print_li[index]

    request.session["print"]=print_li
    request.session["form"]=form_li
    request.session["design_yes"]=design_yes
    d={}
    return JsonResponse(d)


# 最終決定ボタン
def btn_submit(request):
    form_li=request.POST.get("form_li")  
    form_li=json.loads(form_li)
    design_yes=request.POST.get("design_yes")  
    design_yes=json.loads(design_yes)
    shouhin_li=request.session["shouhin"]
    print_li=request.session["print"]

    # Estimation
    ins=Estimation.objects
    if ins.all().count()==0:
        est_num=1
    else:
        est_num=int(ins.aggregate(Max("est_num"))["est_num__max"]) + 1
    ins.create(
        est_num=est_num,
        est_day=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        com=form_li["f_com"],
        busho=form_li["f_busho"],
        tantou=form_li["f_tantou"],
        tel=form_li["f_tel"],
        mail=form_li["f_mail"],
        cus_com=form_li["f_cus_com"],
        cus_name=form_li["f_cus_name"],
        cus_yubin=form_li["f_cus_yubin"],
        cus_adress=form_li["f_cus_adress"],
        cus_tel=form_li["f_cus_tel"],
        cus_send_day=form_li["f_cus_send_day"],
        cus_use_day=form_li["f_cus_use_day"],
        shouhin_tatami=form_li["f_shouhin_tatami"],
        shouhin_bikou=form_li["f_shouhin_bikou"],
        print_bikou=form_li["f_print_bikou"],
        design_yes=design_yes,
    )
    # Shouhin
    for i in shouhin_li:
        all_size=["XXS","XS","S","M","L","LL","3L","4L",i["new_size_1"],i["new_size_2"]]
        Shouhin.objects.create(
            est_num=est_num,
            maker=i["maker"],
            shouhin_num=i["shouhin_num"],
            shouhin_name=i["shouhin_name"],
            color=i["color"],
            size=all_size,
            suryo=i["size_li"],
        )
    # Print
    for i in print_li:
        Print.objects.create(
            est_num=est_num,
            point=i["point"],
            color=i["color"],
            way=i["way"],
        )
    
    # sessionクリア
    request.session["form"]=[]
    request.session["shouhin"]=[]
    request.session["print"]=[]
    request.session["design_yes"]=[False,False,False,False,False]

    d={}
    return JsonResponse(d)


@login_required
# 見積依頼_一覧
def list_index(request):
    est_list=Estimation.objects.all()
    params={"est_list":est_list}
    return render(request,"estimation/list.html",params)


@login_required
# 見積依頼_詳細
def est_detail(request,est_num):
    est_data=Estimation.objects.get(est_num=est_num)
    shouhin_data=Shouhin.objects.filter(est_num=est_num)
    print_data=Print.objects.filter(est_num=est_num)

    shouhin_list=[]
    for i in shouhin_data: 
        # サイズ名
        li_1=["メーカー","品番","品名","カラー"]
        for h in eval(i.size):
            li_1.append(h)
        # 数量
        li_2=[i.maker,i.shouhin_num,i.shouhin_name,i.color]
        for h in eval(i.suryo):
            li_2.append(h)

        shouhin_list.append([li_1,li_2])

    print_list=[]
    for i in print_data:
        print_list.append({"point":i.point,"color":i.color,"way":i.way})

    design_list=[]
    design_type=["イラストレータ（.ai）","フォトショップ（.psd）","画像データ（.jpg / .tiff / .pdf）","手書きデータ","その他（右の備考欄にご記入ください）"]
    design_yes=eval(est_data.design_yes)
    for i in range(len(design_yes)):
        if design_yes[i]==True:
            design_list.append(design_type[i])

    params={
        "est_data":est_data,
        "shouhin_list":shouhin_list,
        "print_list":print_list,
        "design_list":design_list,
    }
    
    return render(request,"estimation/detail.html",params)
