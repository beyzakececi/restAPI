# Generated by Django 4.2.4 on 2023-08-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dronlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=150, verbose_name='Marka')),
                ('model', models.CharField(max_length=300, verbose_name='Model')),
                ('urun_kodu', models.CharField(max_length=50, verbose_name='Ürün Kodu')),
                ('fiyat', models.IntegerField(verbose_name='Fiyat')),
                ('ozellikler', models.TextField(verbose_name='Özellikler')),
            ],
            options={
                'verbose_name_plural': 'Dronlar',
            },
        ),
    ]
