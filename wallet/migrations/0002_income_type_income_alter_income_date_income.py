# Generated by Django 4.0.6 on 2022-08-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='type_income',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='income',
            name='date_income',
            field=models.DateField(verbose_name='Income date.'),
        ),
    ]