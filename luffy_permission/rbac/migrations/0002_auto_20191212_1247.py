# Generated by Django 2.1.7 on 2019-12-12 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(default='', max_length=32, verbose_name='URL别名'),
        ),
    ]