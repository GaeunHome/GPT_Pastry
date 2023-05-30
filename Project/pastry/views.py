from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.models import User 
from .models import Pastry, Order, OrderItem, Member 
from .forms import OrderForm, MemberForm, MemberProfileForm
from django.utils import timezone
# GPT3.5新增
from django.contrib.auth import get_user_model

def index(request): 
    pastries = Pastry.objects.all() 
    return render(request, 'index.html', {'pastries': pastries}) 

def menu(request): 
    pastries = Pastry.objects.all() 
    return render(request, 'menu.html', {'pastries': pastries})
# 根據GPT3.5修改
@login_required
def cart(request):
    try:
        user = request.user
    except Member.DoesNotExist:
        return redirect('login')
    order_items = OrderItem.objects.filter(order__member=user, order__status=False)
    return render(request, 'cart.html', {'order_items': order_items})
'''
# 二次版本
@login_required
def cart(request):
    if not hasattr(request.user, 'member'):
        return redirect('login')
    order_items = OrderItem.objects.filter(order__member=request.user.member, order__status=False)
    return render(request, 'cart.html', {'order_items': order_items})
# 初版
@login_required 
def cart(request): 
    order_items = OrderItem.objects.filter(order__member=request.user.member, order__status=False) 
    return render(request, 'cart.html', {'order_items': order_items}) 
'''
@login_required 
def add_to_cart(request): 
    if request.method == 'POST': 
        form = OrderForm(request.POST) 
        if form.is_valid():
            pastry_id = form.cleaned_data['pastry_id'] 
            quantity = form.cleaned_data['quantity'] 
            pastry = get_object_or_404(Pastry, pk=pastry_id)
            # 新增此段
            # user = get_user_model().objects.get(pk=request.user.pk)
            # 新增timezone.now() # request.user改成user.member
            user = request.user
            order, created = Order.objects.get_or_create(member=user, status=False, defaults={'total_price': 0, 'date': timezone.now()}) 
            order_item, created = OrderItem.objects.get_or_create(order=order, pastry=pastry, defaults={'quantity': 0, 'price': 0}) 
            order_item.quantity += quantity 
            order_item.price = pastry.price * order_item.quantity 
            order_item.save() 
            order.total_price += pastry.price * quantity 
            order.save() 
            messages.success(request, f"{quantity}x {pastry.name} added to cart!") 
            return redirect('cart') 
    else: 
        form = OrderForm() 
    return render(request, 'menu.html', {'form': form}) 

@login_required 
def remove_from_cart(request, order_item_id): 
    order_item = get_object_or_404(OrderItem, pk=order_item_id) 
    order = order_item.order 
    order.total_price -= order_item.price 
    order_item.delete() 
    order.save() 
    messages.success(request, f"{order_item.pastry.name} removed from cart!") 
    return redirect('cart') 

@login_required
def checkout(request):
    if not hasattr(request.user, 'member'):
        return redirect('register')
    if request.method == 'POST':
        
        messages.success(request, "Order placed successfully!")
        return redirect('index')
    else:
        user = request.user
        contact_number = Member.objects.get(user=user).contact_number
        order_items = OrderItem.objects.filter(order__member=request.user, order__status=False)
    return render(request, 'checkout.html', {'order_items': order_items, 'contact_number': contact_number, 'user': user})

def login_view(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid(): 
            user = form.get_user() 
            login(request, user) 
            messages.success(request, f"Welcome back, {user.username}!") 
            return redirect('index') 
    else:
        form = AuthenticationForm() 
    return render(request, 'login.html', {'form': form}) 

def register(request): 
    if request.method == 'POST': 
        form = MemberForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            contact_number = form.cleaned_data['contact_number'] 
            member = Member.objects.create(user=user, contact_number=contact_number) 
            login(request, user) 
            messages.success(request, f"Welcome to our bakery, {user.username}!") 
            return redirect('index') 
    else: 
        form = MemberForm() 
    return render(request, 'register.html', {'form': form}) 

@login_required 
def edit_profile(request): 
    if request.method == 'POST': 
        user_form = UserForm(request.POST, instance=request.user) 
        profile_form = MemberProfileForm(request.POST, instance=request.user.member) 
        if user_form.is_valid() and profile_form.is_valid(): 
            user_form.save() 
            profile_form.save() 
            messages.success(request, "Profile updated successfully!") 
            return redirect('index') 
    else: 
        user_form = UserForm(instance=request.user) 
        profile_form = MemberProfileForm(instance=request.user.member) 
    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form}) 

def view_order(request, order_id): 
    order = get_object_or_404(Order, pk=order_id) 
    if request.user.is_authenticated and request.user == order.member: 
        order_items = OrderItem.objects.filter(order=order) 
        return render(request, 'view_order.html', {'order': order, 'order_items': order_items}) 
    else: 
        return redirect('index') 