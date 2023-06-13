from django.contrib import admin

from credit.models import Contract, CreditRequest, Product, Producer


# Register your models here.


class ContractAdmin(admin.ModelAdmin):
    model = Contract


class CreditRequestAdmin(admin.ModelAdmin):
    model = CreditRequest


class ProductAdmin(admin.ModelAdmin):
    model = Product


class ProducerAdmin(admin.ModelAdmin):
    model = Producer


admin.site.register(Contract, ContractAdmin)
admin.site.register(CreditRequest, CreditRequestAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Producer, ProducerAdmin)
