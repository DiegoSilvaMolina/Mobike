# Generated by Django 2.1 on 2018-08-30 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntregaAtiva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclista', models.CharField(max_length=100)),
                ('end_coleta', models.CharField(max_length=100)),
                ('lat_coleta', models.FloatField()),
                ('end_entrega', models.CharField(max_length=100)),
                ('lat_entrega', models.FloatField()),
                ('lng_coleta', models.FloatField()),
                ('desc', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
