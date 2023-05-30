from django.contrib import admin
from .models import Pastry, Order, OrderItem, Member

class PastryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'date', 'status', 'total_price')
    list_filter = ('status',)
    inlines = [
        OrderItemInline,
    ]

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_number')
    
admin.site.register(Pastry, PastryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Member, MemberAdmin)