# Generated by Django 2.2 on 2019-05-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_prodselectat'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodselectat',
            name='cantitate',
            field=models.IntegerField(default=1),
        ),
    ]