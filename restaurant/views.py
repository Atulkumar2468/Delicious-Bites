from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import MenuItem, Category, About, Contact, Reservation, Order, OrderItem, Chef, Review
import random
import string
from datetime import datetime

def home(request):
    featured_items = MenuItem.objects.filter(is_available=True)[:6]
    categories_count = Category.objects.count()
    chefs = Chef.objects.filter(is_active=True)[:4]
    reviews = Review.objects.filter(is_featured=True, is_approved=True)[:6]
    return render(request, 'restaurant/home.html', {
        'featured_items': featured_items,
        'categories_count': categories_count,
        'chefs': chefs,
        'reviews': reviews,
    })

def menu(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'restaurant/menu.html', {'categories': categories})

def about(request):
    about_info = About.objects.first()
    return render(request, 'restaurant/about.html', {'about': about_info})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    
    return render(request, 'restaurant/contact.html')

def reservations(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        special_requests = request.POST.get('special_requests', '')
        
        # Assign random table number
        table_number = random.randint(1, 20)
        
        reservation = Reservation.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            guests=guests,
            table_number=table_number,
            special_requests=special_requests
        )
        
        # Send email notification
        try:
            send_mail(
                subject='Table Reservation Confirmation - Delicious Bites',
                message=f'''Dear {name},

Thank you for choosing Delicious Bites!

Your table reservation has been confirmed:
- Date: {date}
- Time: {time}
- Guests: {guests}
- Table Number: {table_number}

{f"Special Requests: {special_requests}" if special_requests else ""}

We look forward to serving you!

Best regards,
Delicious Bites Team
Phone: 7004125809''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=True,
            )
        except:
            pass
        
        messages.success(request, f'Your table #{table_number} has been reserved! Confirmation sent to {email} and {phone}.')
        return redirect('reservations')
    
    return render(request, 'restaurant/reservations.html')

# Cart and Order Functions
def get_cart(request):
    return request.session.get('cart', {})

def save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True

def order_food(request):
    categories = Category.objects.prefetch_related('items').all()
    cart = get_cart(request)
    cart_count = sum(item['quantity'] for item in cart.values())
    return render(request, 'restaurant/order_food.html', {
        'categories': categories,
        'cart_count': cart_count
    })

def add_to_cart(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id, is_available=True)
    cart = get_cart(request)
    
    item_id_str = str(item_id)
    if item_id_str in cart:
        cart[item_id_str]['quantity'] += 1
    else:
        cart[item_id_str] = {
            'name': menu_item.name,
            'price': float(menu_item.price),
            'quantity': 1
        }
    
    save_cart(request, cart)
    messages.success(request, f'{menu_item.name} added to cart!')
    return redirect('order_food')

def update_cart(request, item_id):
    if request.method == 'POST':
        cart = get_cart(request)
        item_id_str = str(item_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart[item_id_str]['quantity'] = quantity
        else:
            del cart[item_id_str]
        
        save_cart(request, cart)
    return redirect('view_cart')

def remove_from_cart(request, item_id):
    cart = get_cart(request)
    item_id_str = str(item_id)
    
    if item_id_str in cart:
        del cart[item_id_str]
        save_cart(request, cart)
        messages.success(request, 'Item removed from cart!')
    
    return redirect('view_cart')

def view_cart(request):
    cart = get_cart(request)
    cart_items = []
    total = 0
    
    for item_id, item_data in cart.items():
        subtotal = item_data['price'] * item_data['quantity']
        cart_items.append({
            'id': item_id,
            'name': item_data['name'],
            'price': item_data['price'],
            'quantity': item_data['quantity'],
            'subtotal': subtotal
        })
        total += subtotal
    
    return render(request, 'restaurant/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

def checkout(request):
    cart = get_cart(request)
    if not cart:
        messages.warning(request, 'Your cart is empty!')
        return redirect('order_food')
    
    cart_items = []
    total = 0
    
    for item_id, item_data in cart.items():
        subtotal = item_data['price'] * item_data['quantity']
        cart_items.append({
            'id': item_id,
            'name': item_data['name'],
            'price': item_data['price'],
            'quantity': item_data['quantity'],
            'subtotal': subtotal
        })
        total += subtotal
    
    return render(request, 'restaurant/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

def payment(request):
    if request.method == 'POST':
        cart = get_cart(request)
        if not cart:
            messages.warning(request, 'Your cart is empty!')
            return redirect('order_food')
        
        # Get customer details
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        table_number = int(request.POST.get('table_number'))
        payment_method = request.POST.get('payment_method')
        
        # Generate order ID
        order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        
        # Calculate total
        total = sum(item['price'] * item['quantity'] for item in cart.values())
        
        # Create order
        order = Order.objects.create(
            order_id=order_id,
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            table_number=table_number,
            total_amount=total,
            payment_method=payment_method,
            payment_status='completed'
        )
        
        # Create order items
        for item_id, item_data in cart.items():
            menu_item = MenuItem.objects.get(id=int(item_id))
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=item_data['quantity'],
                price=item_data['price']
            )
        
        # Send confirmation email
        try:
            items_text = '\n'.join([f"  {item['quantity']}x {item['name']} - ₹{item['price'] * item['quantity']:.2f}" 
                                   for item in cart.values()])
            
            send_mail(
                subject=f'Order Confirmation - {order_id}',
                message=f'''Dear {customer_name},

Thank you for your order at Delicious Bites!

Order ID: {order_id}
Table Number: {table_number}
Date: {datetime.now().strftime("%Y-%m-%d %H:%M")}

Items Ordered:
{items_text}

Total Amount: ₹{total:.2f}
Payment Method: {payment_method}
Payment Status: Completed

Your order will be served shortly!

Best regards,
Delicious Bites Team
Phone: 7004125809''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[customer_email],
                fail_silently=True,
            )
        except:
            pass
        
        # Clear cart
        request.session['cart'] = {}
        request.session.modified = True
        
        return redirect('receipt', order_id=order_id)
    
    return redirect('checkout')

def receipt(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    order_items = order.items.all()
    
    return render(request, 'restaurant/receipt.html', {
        'order': order,
        'order_items': order_items
    })

