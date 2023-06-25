# Generated by Django 3.2.16 on 2023-06-25 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0003_alter_sensor_local'),
        ('DataLogSensor', '0008_auto_20230610_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='data',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='direcao',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Direção do vento'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='estacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Device.sensor', verbose_name='Identificação da Estação'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='hora',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Hora'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='pressao_max',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Pressão Máxima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='pressao_media',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Pressao Média'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='pressao_min',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Pressão Mínima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='temp_max',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Temperatura Máxima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='temp_media',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Temperatura Média'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='temp_min',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Temperatura Mínima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='umidade_max',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Umidade Máxima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='umidade_media',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Umidade Média'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='umidade_min',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Umidade Mínima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='uv',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='UV'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='vm_max',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Velocidade Máxima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='vm_media',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Velocidade Média'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='vm_min',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Velocidade Mínima'),
        ),
        migrations.AlterField(
            model_name='registro',
            name='w_m2',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='W/m2'),
        ),
    ]