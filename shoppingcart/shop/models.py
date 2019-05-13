from django.db import models

class Tip(models.Model):
    id = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=50)
    datacreare = models.DateTimeField(auto_now_add=True)
    datamodificare = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nume',)
        verbose_name = 'tip'
        verbose_name_plural = 'tipuri'

    def __str__(self):
        return self.nume


class Produs(models.Model):
    id = models.AutoField(primary_key=True)
    tip = models.ForeignKey(Tip, related_name='produse', on_delete=models.CASCADE)
    nume = models.CharField(max_length=100, db_index=True)
    descriere = models.TextField(blank=True)
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    disponibil = models.BooleanField(default=True)
    datacreare = models.DateTimeField(auto_now_add=True)
    datamodificare = models.DateTimeField(auto_now=True)
    imagine = models.ImageField(upload_to='produse/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('nume',)
        verbose_name = 'produs'
        verbose_name_plural = 'produse'
        index_together = (('id'),)


    def __str__(self):
        return self.nume


class Prodselectat(models.Model):
    id = models.AutoField(primary_key=True)
    idp = models.IntegerField()
    tip = models.ForeignKey(Tip, related_name='prodselectat', on_delete=models.CASCADE)
    nume = models.CharField(max_length=100, db_index=True)
    pret = models.DecimalField(max_digits=10, decimal_places=2)
    cantitate=models.IntegerField(default=1)
    dataselect = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'prodselectat'
        verbose_name_plural = 'produseselectate'


    def __str__(self):
        return self.nume


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id'),)

    def __str__(self):
        return self.name

