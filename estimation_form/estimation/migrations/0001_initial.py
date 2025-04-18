# Generated by Django 4.2.1 on 2025-03-24 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='見積No')),
                ('com', models.CharField(blank=True, max_length=255, null=True, verbose_name='会社名')),
                ('busho', models.CharField(blank=True, max_length=255, null=True, verbose_name='部署')),
                ('tantou', models.CharField(blank=True, max_length=255, null=True, verbose_name='担当者')),
                ('mail', models.CharField(blank=True, max_length=255, null=True, verbose_name='メール')),
                ('cus_com', models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客_会社名')),
                ('cus_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客_氏名')),
                ('cus_yubin', models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客_郵便番号')),
                ('cus_adress', models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客_住所')),
                ('cus_tel', models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客_電話番号')),
                ('cus_send_day', models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客_納期')),
                ('cus_use_day', models.CharField(blank=True, max_length=255, null=True, verbose_name='顧客_使用日')),
                ('shouhin_tatami', models.IntegerField(default=0, verbose_name='商品_たたみ袋')),
                ('shouhin_bikou', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品_備考')),
                ('print_data', models.CharField(blank=True, max_length=255, null=True, verbose_name='プリント_入稿データ')),
                ('print_bikou', models.CharField(blank=True, max_length=255, null=True, verbose_name='プリント_備考')),
            ],
        ),
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='見積No')),
                ('point', models.CharField(blank=True, max_length=255, null=True, verbose_name='プリント箇所')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='見積No')),
                ('way', models.CharField(blank=True, max_length=255, null=True, verbose_name='見積No')),
            ],
        ),
        migrations.CreateModel(
            name='Shouhin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='見積No')),
                ('maker', models.CharField(blank=True, max_length=255, null=True, verbose_name='メーカー')),
                ('shouhin_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品番号')),
                ('shouhin_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品名')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='カラー')),
                ('size', models.CharField(blank=True, max_length=255, null=True, verbose_name='サイズ')),
                ('suryo', models.IntegerField(default=0, verbose_name='数量')),
            ],
        ),
    ]
