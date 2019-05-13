from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=100, db_index=True)
    telefon=models.CharField(max_length=100,db_index=True)
    bursa = models.DecimalField(max_digits=10, decimal_places=2)
    localitate=models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('nume',)
        verbose_name = 'student'
        verbose_name_plural = 'studenti'


    def __str__(self):
        return self.nume
