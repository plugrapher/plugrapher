# Generated by Django 3.2.22 on 2023-10-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0011_auto_20231012_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='paymentTerms',
        ),
        migrations.AddField(
            model_name='product',
            name='rates',
            field=models.CharField(choices=[('15 days', '15 days'), ('30 days', '30 days'), ('60 days', '60 days'), ('90 days', '90 days'), ('120 days', '120 days'), ('150 days', '150 days'), ('180 days', '180 days')], default='14 days', max_length=100),
        ),
    ]
