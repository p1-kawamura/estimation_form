# Generated by Django 4.2.1 on 2025-03-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estimation', '0005_alter_print_color_alter_print_way'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimation',
            name='print_data',
        ),
        migrations.AddField(
            model_name='estimation',
            name='design_yes',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='入稿データ'),
        ),
    ]
