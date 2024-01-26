# Generated by Django 5.0.1 on 2024-01-25 22:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fabricante', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('preco', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('fabricante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.fabricante')),
            ],
        ),
    ]