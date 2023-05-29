# Generated by Django 4.2.1 on 2023-05-23 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AEPDE_APP', '0022_transportista_tarifa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarifa',
            options={'permissions': [('puede_acceder_url', 'Puede acceder a la URL')]},
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(auto_created=True)),
                ('nuevo_precio', models.IntegerField()),
                ('fecha_fin', models.DateField()),
                ('cod_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AEPDE_APP.producto')),
            ],
        ),
    ]
