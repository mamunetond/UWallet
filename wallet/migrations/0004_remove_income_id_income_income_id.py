# Generated by Django 4.0.6 on 2022-09-06 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_spent_type_spent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='id',
        ),
        migrations.AddField(
            model_name='income',
            name='income_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
