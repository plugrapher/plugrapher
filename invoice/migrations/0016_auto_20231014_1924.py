# Generated by Django 3.2.22 on 2023-10-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0015_alter_product_rates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='province',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='settings',
            old_name='province',
            new_name='county',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paymentTerms',
            field=models.CharField(choices=[('15 days', '15 days'), ('30 days', '30 days'), ('60 days', '60 days'), ('90 days', '90 days'), ('120 days', '120 days'), ('150 days', '150 days'), ('180 days', '180 days')], default='15 days', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('Kes', 'ksh'), ('$', 'USD')], default='KSH', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='rates',
            field=models.CharField(choices=[('35', '15 days - ksh 35 per kilo'), ('40', '30 days - ksh 40 per kilo'), ('50', '60 days - ksh 50 per kilo'), ('60', '90 days - ksh 60 per kilo'), ('70', '120 days - ksh 70 per kilo'), ('80', '150 days - ksh 80 per kilo'), ('90', '180 days - ksh 90 per kilo')], default='35', max_length=100),
        ),
    ]