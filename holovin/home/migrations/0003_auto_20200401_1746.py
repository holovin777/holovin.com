# Generated by Django 2.2.8 on 2020-04-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homeimage_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeimage',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
