# Generated by Django 5.0.4 on 2024-05-03 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='codPos',
            field=models.IntegerField(default=45060),
        ),
        migrations.AddField(
            model_name='employee',
            name='edad',
            field=models.IntegerField(default=22),
        ),
        migrations.AddField(
            model_name='employee',
            name='numeroExt',
            field=models.IntegerField(default=1234),
        ),
        migrations.AddField(
            model_name='employee',
            name='telefono',
            field=models.IntegerField(default=3331000000),
        ),
    ]
