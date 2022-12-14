# Generated by Django 4.0.6 on 2022-08-16 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_income', models.IntegerField(default=0)),
                ('detail_income', models.CharField(max_length=200)),
                ('date_income', models.DateTimeField(verbose_name='Income date.')),
            ],
        ),
        migrations.CreateModel(
            name='Spent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_spent', models.IntegerField(default=0)),
                ('detail_spent', models.CharField(max_length=200)),
                ('date_spent', models.DateField(verbose_name='Spent date.')),
            ],
        ),
    ]
