# Generated by Django 3.2.16 on 2023-04-30 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataLogSensor', '0004_auto_20230429_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='date',
            field=models.CharField(blank=True, max_length=10, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='direcao',
            field=models.CharField(blank=True, max_length=8, verbose_name='Direção'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='mm_dia',
            field=models.CharField(blank=True, max_length=8, verbose_name='mm/dia'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='mm_h',
            field=models.CharField(blank=True, max_length=8, verbose_name='mm/hora'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='pressao',
            field=models.CharField(blank=True, max_length=8, verbose_name='Pressao'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='temp',
            field=models.CharField(blank=True, max_length=8, verbose_name='Temperatura'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='umidade',
            field=models.CharField(blank=True, max_length=8, verbose_name='Umidade'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='uv',
            field=models.CharField(blank=True, max_length=8, verbose_name='UV'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='vmax',
            field=models.CharField(blank=True, max_length=8, verbose_name='Velocidade máxima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='vmed',
            field=models.CharField(blank=True, max_length=8, verbose_name='Velocidade média'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='w_m2',
            field=models.CharField(blank=True, max_length=8, verbose_name='W/m2'),
        ),
    ]
