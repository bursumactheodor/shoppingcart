# Generated by Django 2.2 on 2019-05-10 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nume', models.CharField(max_length=50)),
                ('datacreare', models.DateTimeField(auto_now_add=True)),
                ('datamodificare', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'tip',
                'verbose_name_plural': 'tipuri',
                'ordering': ('nume',),
            },
        ),
        migrations.CreateModel(
            name='Produs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nume', models.CharField(db_index=True, max_length=100)),
                ('descriere', models.TextField(blank=True)),
                ('pret', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponibil', models.BooleanField(default=True)),
                ('datacreare', models.DateTimeField(auto_now_add=True)),
                ('datamodificare', models.DateTimeField(auto_now=True)),
                ('imagine', models.ImageField(blank=True, upload_to='produse/%Y/%m/%d')),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produse', to='shop.Tip')),
            ],
            options={
                'ordering': ('nume',),
                'index_together': {('id',)},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.Category')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id',)},
            },
        ),
    ]
