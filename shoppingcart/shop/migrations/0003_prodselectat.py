# Generated by Django 2.2 on 2019-05-13 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190510_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prodselectat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idp', models.IntegerField()),
                ('nume', models.CharField(db_index=True, max_length=100)),
                ('pret', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dataselect', models.DateTimeField(auto_now_add=True)),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prodselectat', to='shop.Tip')),
            ],
            options={
                'verbose_name': 'prodselectat',
                'verbose_name_plural': 'produseselectate',
            },
        ),
    ]