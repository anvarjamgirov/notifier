# Generated by Django 3.1.3 on 2020-11-24 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='64 belgidan oshmasligi kerak', max_length=64, verbose_name='Nomi')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='64 ta belgidan oshmasligi kerak', max_length=64, verbose_name='Ism')),
                ('last_name', models.CharField(help_text='64 ta belgidan oshmasligi kerak', max_length=64, verbose_name='Familiya')),
                ('email', models.EmailField(max_length=254)),
                ('categories', models.ManyToManyField(help_text="Bir nechta bo'lim tanlashda shift+enter dan foydalaning", related_name='followers', to='core.Category', verbose_name="Yoqtirgan bo'limlari")),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='64 belgidan oshmasligi kerak', max_length=64, verbose_name='Nomi')),
                ('description', models.TextField(help_text="Mahsulot haqida qisqacha ma'lumot, kiritilishi shart", verbose_name="Qisqacha ma'lumot")),
                ('price', models.FloatField(default=0.0, verbose_name='Narxi')),
                ('category', models.ForeignKey(help_text="Mahsulot mansub bo'lgan bo'lim, biriktirilishi shart", on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.category', verbose_name="Bo'lim")),
            ],
        ),
    ]