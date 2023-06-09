# Generated by Django 4.2.1 on 2023-05-09 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('cod_sucursal', models.IntegerField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('fecha_produccion', models.DateTimeField(auto_created=True)),
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('1', 'Frutas'), ('2', 'Verduras'), ('3', 'Cereales')], default=1, max_length=1)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('fecha_vencimiento_prod', models.DateTimeField()),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AEPDE_APP.sucursal')),
            ],
        ),
    ]
