from django.contrib import admin
from cars.models import Car, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value') # lista que será mostrado na tabela
    search_fields = ('model', ) # campo de busca

admin.site.register(Car, CarAdmin) # Para registrar no site, ela pede dois campos, qual a tabela de modelos, e qual a classe das configurações de admin
admin.site.register(Brand, BrandAdmin)