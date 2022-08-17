from django.contrib import admin
from .models import Product,Order
# Register your models here.

admin.site.site_header="E-commerce Site"
admin.site.site_title="ABC Shopping"
admin.site.index_title="Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")
    
    change_category_to_default.short_description ='default category'
    list_display = ('title','price','discount_price','category','discription')
    search_fields = ['title','price','category']
    actions = ('change_category_to_default',)
    #fields =('title','price',)      #only display this two field in database
    list_editable =('price','category',)
    
    
class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('items','name','email','city','state','total')
    search_fields = ['items','city','state']
    
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
# admin.site.register(Order)