from django.contrib import admin

from .models import Customer, Product, Order
class UserAdmin(admin.ModelAdmin):
    list_display="name","email","phone_number","address"
admin.site.register(Customer,UserAdmin)
class ProductAdmin(admin.ModelAdmin):
    list_display="name","price","stock_quantity","description"
  
admin.site.register(Product,ProductAdmin)   
 
#  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     order_date = models.DateField(auto_now_add=True)
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Completed', 'Completed'),
#     ]
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES)
class OrderAdmin(admin.ModelAdmin):
    list_display="customer","product","quantity","order_date","status" 
admin.site.register(Order,OrderAdmin)   