# Generated by Django 4.2.1 on 2023-05-16 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AEPDE_APP', '0018_alter_productor_telefono_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productor',
            name='cod_productor',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productor',
            name='telefono_contacto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='cod_sucursal',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
