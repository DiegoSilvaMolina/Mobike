# Generated by Django 2.1 on 2018-09-03 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_entregaativa_lng_entrega'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entregaativa',
            name='lat_coleta',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='entregaativa',
            name='lat_entrega',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='entregaativa',
            name='lng_coleta',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='entregaativa',
            name='lng_entrega',
            field=models.FloatField(null=True),
        ),
    ]