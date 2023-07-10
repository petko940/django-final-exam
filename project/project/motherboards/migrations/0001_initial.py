# Generated by Django 4.2.1 on 2023-07-09 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(choices=[('ASUS', 'ASUS'), ('GIGABYTE', 'GIGABYTE'), ('MSI', 'MSI'), ('ASRock', 'ASRock'), ('Intel', 'Intel'), ('Acer', 'Acer'), ('EVGA', 'EVGA'), ('Biostar', 'Biostar'), ('American Megatrends', 'American Megatrends')], max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('form_factor', models.CharField(choices=[('Micro-ATX', 'Micro-ATX'), ('ATX', 'ATX'), ('Mini-ITX', 'Mini-ITX'), ('E-ATX', 'E-ATX')], max_length=20)),
                ('chipset', models.CharField(max_length=20)),
                ('socket', models.CharField(max_length=10)),
                ('networking', models.CharField(choices=[('Ethernet', 'Ethernet'), ('Wi-Fi', 'Wi-Fi'), ('Ethernet/Wi-Fi', 'Ethernet/Wi-Fi')], max_length=20)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]