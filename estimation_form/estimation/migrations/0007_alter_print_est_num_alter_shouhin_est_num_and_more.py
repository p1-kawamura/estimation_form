# Generated by Django 4.2.1 on 2025-03-27 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimation', '0006_remove_estimation_print_data_estimation_design_yes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='est_num',
            field=models.IntegerField(default=0, verbose_name='見積番号'),
        ),
        migrations.AlterField(
            model_name='shouhin',
            name='est_num',
            field=models.IntegerField(default=0, verbose_name='見積番号'),
        ),
        migrations.AlterField(
            model_name='shouhin',
            name='suryo',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='数量'),
        ),
    ]
