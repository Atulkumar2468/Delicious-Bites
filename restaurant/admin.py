from django.contrib import admin
from .models import Category, MenuItem, About, Contact, Reservation, Order, OrderItem, Chef, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'created_at']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date', 'time', 'guests', 'table_number', 'status', 'created_at']
    list_filter = ['status', 'date']
    search_fields = ['name', 'email', 'phone']
    list_editable = ['status', 'table_number']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['menu_item', 'quantity', 'price']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'customer_name', 'table_number', 'total_amount', 'payment_status', 'created_at']
    list_filter = ['payment_status', 'created_at']
    search_fields = ['order_id', 'customer_name', 'customer_email']
    readonly_fields = ['order_id', 'created_at']
    inlines = [OrderItemInline]

@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience_years', 'specialty', 'is_active', 'order']
    list_filter = ['is_active', 'position']
    search_fields = ['name', 'position', 'specialty']
    list_editable = ['order', 'is_active']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'rating', 'is_featured', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_featured', 'is_approved', 'created_at']
    search_fields = ['customer_name', 'comment']
    list_editable = ['is_featured', 'is_approved']
    readonly_fields = ['created_at']
