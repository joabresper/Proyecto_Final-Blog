# Generated by Django 3.1 on 2021-12-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
    ]