# Generated by Django 4.0.3 on 2022-12-01 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documento', '0007_alter_documento_encargado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='ruc',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
