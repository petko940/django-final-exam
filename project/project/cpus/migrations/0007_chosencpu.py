# Generated by Django 4.2.1 on 2023-06-28 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cpus', '0006_remove_allcpus_chosen_pc_by_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChosenCpu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpus.allcpus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
