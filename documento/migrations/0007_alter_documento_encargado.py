# Generated by Django 4.0.3 on 2022-10-31 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0006_factura_area_factura_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='encargado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documento.area'),
        ),
    ]