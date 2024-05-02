# Generated by Django 5.0.4 on 2024-05-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('calle', models.CharField(max_length=100)),
                ('numeroInt', models.CharField(max_length=10)),
                ('colonia', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=54)),
                ('fechaNac', models.DateField()),
            ],
        ),
    ]
