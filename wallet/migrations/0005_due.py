# Generated by Django 4.0.6 on 2022-11-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_goal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Due',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_due', models.CharField(max_length=50)),
                ('number_due', models.IntegerField(default=0)),
                ('date_due', models.DateField(verbose_name='Due date.')),
                ('detail_due', models.DateField(max_length=200)),
            ],
        ),
    ]
