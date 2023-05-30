from django.contrib import admin
from .models import Pastry, Member, Order, OrderItem 

# Register your models here.
class PastryAdmin(admin.ModelAdmin):
    list_display = ('CATEGORY_CHOICES', 'name', 'category', 'description', 'price')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_number')

admin.site.register(Pastry, PastryAdmin)
admin.site.register(Member, MemberAdmin)
# admin.site.register(Member, MemberAdmin)
# admin.site.register(Member, MemberAdmin)