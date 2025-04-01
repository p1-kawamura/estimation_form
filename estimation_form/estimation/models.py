from django.db import models

class Estimation(models.Model):
    est_num=models.IntegerField("見積番号",default=0)
    est_day=models.CharField("見積日時",max_length=255,blank=True,null=True)
    com=models.CharField("会社名",max_length=255,blank=True,null=True)
    busho=models.CharField("部署",max_length=255,blank=True,null=True)
    tantou=models.CharField("担当者",max_length=255,blank=True,null=True)
    tel=models.CharField("電話番号",max_length=255,blank=True,null=True)
    mail=models.CharField("メール",max_length=255,blank=True,null=True)
    cus_com=models.CharField("顧客_会社名",max_length=255,blank=True,null=True)
    cus_name=models.CharField("顧客_氏名",max_length=255,blank=True,null=True)
    cus_yubin=models.CharField("顧客_郵便番号",max_length=255,blank=True,null=True)
    cus_adress=models.CharField("顧客_住所",max_length=255,blank=True,null=True)
    cus_tel=models.CharField("顧客_電話番号",max_length=255,blank=True,null=True)
    cus_send_day=models.CharField("顧客_納期",max_length=255,blank=True,null=True)
    cus_use_day=models.CharField("顧客_使用日",max_length=255,blank=True,null=True)
    shouhin_tatami=models.CharField("商品_たたみ袋",max_length=255,blank=True,null=True)
    shouhin_bikou=models.CharField("商品_備考",max_length=255,blank=True,null=True)
    print_bikou=models.CharField("プリント_備考",max_length=255,blank=True,null=True)
    design_yes=models.CharField("入稿データ",max_length=255,blank=True,null=True)

    def __str__(self):
        return str(self.est_num)



class Shouhin(models.Model):
    est_num=models.IntegerField("見積番号",default=0)
    maker=models.CharField("メーカー",max_length=255,blank=True,null=True)
    shouhin_num=models.CharField("商品番号",max_length=255,blank=True,null=True)
    shouhin_name=models.CharField("商品名",max_length=255,blank=True,null=True)
    color=models.CharField("カラー",max_length=255,blank=True,null=True)
    size=models.CharField("サイズ",max_length=255,blank=True,null=True)
    suryo=models.CharField("数量",max_length=255,blank=True,null=True)

    def __str__(self):
        return str(self.est_num)



class Print(models.Model):
    est_num=models.IntegerField("見積番号",default=0)
    point=models.CharField("プリント箇所",max_length=255,blank=True,null=True)
    color=models.CharField("プリント色",max_length=255,blank=True,null=True)
    way=models.CharField("加工方法",max_length=255,blank=True,null=True)

    def __str__(self):
        return str(self.est_num)
    


class Member(models.Model):
    user_id=models.CharField("ユーザーID",max_length=255,blank=True,null=True)
    user_com=models.CharField("会社名",max_length=255,blank=True,null=True)

    def __str__(self):
        return str(self.user_id)