# Generated by Django 4.2.1 on 2023-05-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AEPDE_APP', '0008_alter_producto_fecha_vencimiento_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_produccion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_vencimiento_prod',
            field=models.DateField(),
        ),
    ]