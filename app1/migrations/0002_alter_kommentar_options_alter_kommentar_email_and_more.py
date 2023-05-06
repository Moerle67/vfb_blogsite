# Generated by Django 4.2 on 2023-05-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kommentar',
            options={'verbose_name_plural': 'Kommentare'},
        ),
        migrations.AlterField(
            model_name='kommentar',
            name='email',
            field=models.CharField(max_length=50, verbose_name='E-Mail Adresse'),
        ),
        migrations.AlterField(
            model_name='kommentar',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nutzer, der wo eingetragen hat'),
        ),
        migrations.AlterField(
            model_name='kommentar',
            name='ueberschrift',
            field=models.CharField(max_length=30, verbose_name='Überschrift'),
        ),
    ]