# Generated by Django 4.2.1 on 2023-05-11 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AEPDE_APP', '0014_productor'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cod_productor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AEPDE_APP.productor'),
            preserve_default=False,
        ),
    ]