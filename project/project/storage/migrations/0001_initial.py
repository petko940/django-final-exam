# Generated by Django 4.2.1 on 2023-07-07 09:52

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
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=3)),
                ('brand', models.CharField(choices=[('Western Digital', 'Western Digital'), ('Seagate', 'Seagate'), ('Toshiba', 'Toshiba'), ('Samsung', 'Samsung'), ('Fujitsu', 'Fujitsu'), ('Kingston', 'Kingston'), ('Crucial', 'Crucial'), ('SanDisk', 'SanDisk'), ('ADATA', 'ADATA'), ('Corsair', 'Corsair')], max_length=20)),
                ('capacity', models.PositiveIntegerField()),
                ('interface', models.CharField(choices=[('SATA', 'SATA'), ('PCIe', 'PCIe'), ('NVMe', 'NVMe'), ('USB', 'USB'), ('Thunderbolt', 'Thunderbolt')], max_length=20)),
                ('read_speed', models.PositiveIntegerField(blank=True, null=True, verbose_name='Read speed')),
                ('write_speed', models.PositiveIntegerField(blank=True, null=True, verbose_name='Write speed')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]