# Generated by Django 4.2.1 on 2023-07-02 08:34

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
            name='AllGpus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(blank=True, choices=[('Nvidia', 'Nvidia'), ('AMD', 'AMD'), ('ATI', 'ATI'), ('Intel', 'Intel')], null=True)),
                ('name', models.CharField(blank=True, max_length=25, null=True)),
                ('release_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='Release year')),
                ('memory_size', models.PositiveIntegerField(blank=True, null=True, verbose_name='Memory size')),
                ('memory_bus_width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Memory bus width')),
                ('gpu_clock', models.PositiveIntegerField(blank=True, null=True, verbose_name='GPU clock')),
                ('memory_clock', models.PositiveIntegerField(blank=True, null=True, verbose_name='Memory clock')),
                ('memory_type', models.CharField(blank=True, null=True, verbose_name='Memory type')),
            ],
        ),
        migrations.CreateModel(
            name='ChosenGpus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpus.allgpus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
