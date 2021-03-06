# Generated by Django 2.1 on 2018-09-16 03:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180915_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrega',
            name='urgencia',
        ),
        migrations.AddField(
            model_name='entregaativa',
            name='status',
            field=models.CharField(choices=[('D', 'Disponivel'), ('E', 'Em andamento')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='entregaativa',
            name='ciclista',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Ciclista'),
        ),
        migrations.AlterField(
            model_name='entregaativa',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
