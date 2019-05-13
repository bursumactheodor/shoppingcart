from django.contrib import admin

from .models import Tip
from .models import Produs
from .models import Category
from .models import Product

admin.site.register(Tip)
admin.site.register(Produs)
admin.site.register(Category)
admin.site.register(Product)



# Register your models here.
