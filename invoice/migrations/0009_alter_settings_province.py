# Generated by Django 3.2.22 on 2023-10-11 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_auto_20231012_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='province',
            field=models.CharField(blank=True, choices=[('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Eldoret', 'Eldoret'), ('Kisumu', 'Kisumu')], max_length=100),
        ),
    ]
