# Generated by Django 4.2.5 on 2023-09-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_delete_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_date',
            field=models.DateField(),
        ),
    ]