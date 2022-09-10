# Generated by Django 4.0.3 on 2022-09-10 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, null=True)),
                ('nombre', models.CharField(max_length=30, null=True)),
                ('apellido_pater', models.CharField(max_length=30, null=True)),
                ('apellido_mater', models.CharField(max_length=30, null=True)),
                ('celular', models.CharField(max_length=9, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='')),
                ('data_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EncargadoArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, null=True)),
                ('nombre', models.CharField(max_length=30, null=True)),
                ('apellido_pater', models.CharField(max_length=30, null=True)),
                ('apellido_mater', models.CharField(max_length=30, null=True)),
                ('celular', models.CharField(max_length=9, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='')),
                ('data_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=30, null=True)),
                ('contacto', models.CharField(max_length=9, null=True)),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='')),
                ('data_created', models.DateField(auto_now_add=True, null=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documento.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, null=True)),
                ('tipo', models.CharField(choices=[('opcion1', 'opcion1'), ('opcion2', 'opcion2'), ('opcion3', 'opcion3'), ('opcion4', 'opcion4')], max_length=20, null=True)),
                ('estado', models.CharField(choices=[('Evaluando', 'Evaluando'), ('Aprobado', 'Aprobado'), ('Rechazado', 'Rechazado'), ('Observado', 'Observado')], max_length=20, null=True)),
                ('pedido', models.CharField(max_length=300, null=True)),
                ('encargado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documento.encargadoarea')),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documento.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('encargado', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='documento.encargadoarea')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='data joined')),
                ('last_login', models.DateTimeField(auto_now_add=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
