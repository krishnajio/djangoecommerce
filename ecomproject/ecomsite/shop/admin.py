from django.contrib import admin
from .models import Products,Order,OrderUpdate
# Register your models here.

#Admin panel Customization
admin.site.site_header ='E Commerce Site'
admin.site.site_title = 'ABC Shoping'
admin.site.index_title = 'Manage ABC Shoping'

class ProductAdmin(admin.ModelAdmin):
    
    def chage_category_to_default(self,request,queryset):
        queryset.update(category='default')
    
    list_display = ('title','price','discount_price','category','description')
    search_fields = ('title',)
    action = ('chage_category_to_default',)  
    list_editable= ('price',)  
    
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderUpdate)

