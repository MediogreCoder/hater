# Generated by Django 4.0.4 on 2022-05-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hater_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hates',
            name='h_body',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='hates',
            name='hate_date',
            field=models.DateTimeField(default='2022-05-06 18:20'),
        ),
    ]
