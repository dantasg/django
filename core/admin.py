from django.contrib import admin
from django.contrib.admin.filters import ListFilter

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


from .models import Produto, Cliente

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)

