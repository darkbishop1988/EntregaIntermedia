# Generated by Django 4.1.3 on 2022-12-04 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_adopcion_edad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adopcion',
            old_name='nombreMascota',
            new_name='nombre_de_Mascota',
        ),
        migrations.RenameField(
            model_name='adopcion',
            old_name='nombreTutelar',
            new_name='nombre_del_Tutelar',
        ),
    ]
