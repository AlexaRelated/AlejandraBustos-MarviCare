# Generated by Django 5.0.6 on 2024-08-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesoformacion',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='accesoformacion',
            name='fecha_inicio',
        ),
        migrations.AddField(
            model_name='accesoformacion',
            name='email',
            field=models.EmailField(default=1, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]