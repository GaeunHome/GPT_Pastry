from django.db import models 
from django.contrib.auth.models import User 

class Pastry(models.Model): 
    CATEGORY_CHOICES = [ 
        ('cake', 'Cake'), 
        ('pie', 'Pie'), 
        ('cookie', 'Cookie'), 
    ] 
    name = models.CharField(max_length=255) 
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES) 
    description = models.TextField() 
    price = models.IntegerField() 
    image = models.ImageField(upload_to='images/', default=False) 
    def __str__(self): 
        return self.name 
    
class Order(models.Model): 
    member = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateField() 
    status = models.BooleanField(default=False)
    total_price = models.IntegerField() 
    def __str__(self): 
        return f"Order {self.id} by {self.member.username}" 
    
class OrderItem(models.Model): 
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    pastry = models.ForeignKey(Pastry, on_delete=models.CASCADE) 
    quantity = models.IntegerField() 
    price = models.IntegerField() 
    def __str__(self): 
        return f"{self.quantity}x {self.pastry.name} for Order {self.order.id}"
    
class Member(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    contact_number = models.CharField(max_length=20)
    def __str__(self): 
        return self.user.username 