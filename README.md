# Delicious-Bites
# Restaurant Website - Django

A complete, full-featured restaurant website built with Django featuring online ordering, table reservations, payment processing, and automated notifications.

## 🌟 Features

### Customer Features
- 🏠 **Beautiful Home Page** - Hero section, restaurant stats, and featured dishes
- 🍽️ **Full Menu** - Browse menu organized by categories (Appetizers, Main Courses, Desserts, Beverages)
- 🛒 **Online Food Ordering** - Add items to cart, manage quantities, and place orders
- 💳 **Payment System** - Multiple payment methods (Cash, Credit/Debit Card, Digital Wallet)
- 🧾 **Digital Receipt** - Detailed receipt with Order ID, items, and table number
- 📅 **Table Reservations** - Book tables with date/time selection and automatic table assignment
- 📧 **Email Notifications** - Automatic confirmation emails for orders and reservations
- 📱 **SMS Notifications** - Phone number confirmation for reservations
- 📖 **About Page** - Restaurant story and information
- 📧 **Contact Form** - Customer inquiry form

### Admin Features
- 👨‍💼 **Complete Admin Panel** - Manage all content from one place
- 📊 **Order Management** - View all orders with details and payment status
- 🪑 **Reservation Management** - Manage bookings, assign tables, update status
- 🍴 **Menu Management** - Add/edit categories and menu items with images
- 📬 **Contact Submissions** - View customer inquiries
- 🖼️ **Image Upload** - Support for menu item images

## 🚀 Quick Start

1. **Activate virtual environment:**
   ```bash
   .venv\Scripts\activate
   ```

2. **Create admin user:**
   ```bash
   python manage.py createsuperuser
   ```
   Enter username, email, and password when prompted.

3. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

4. **Access the website:**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📦 Pre-loaded Sample Data

The database includes:
- ✅ 4 menu categories
- ✅ 18 delicious menu items with descriptions and prices
- ✅ About page content

## 🛍️ How to Use the Ordering System

### For Customers:
1. Click "Order Food" in navigation or home page
2. Browse menu and click "Add to Cart" on desired items
3. View cart and update quantities if needed
4. Proceed to checkout
5. Enter customer details and table number
6. Select payment method
7. Complete payment
8. Receive digital receipt with Order ID
9. Get confirmation email

### For Restaurant Staff (Admin):
1. Login to admin panel
2. View orders in "Orders" section
3. See order details, items, payment status
4. Manage reservations and assign tables
5. Update order/reservation status

## 📅 Table Reservation System

### Features:
- Date and time selection
- Guest count selection
- Special requests field
- Automatic table number assignment
- Email confirmation with reservation details
- SMS notification to phone number
- Reservation status management (Pending/Confirmed/Cancelled)

## 💳 Payment Methods Supported

- 💵 Cash
- 💳 Credit Card
- 💳 Debit Card
- 📱 Digital Wallet (UPI, PayPal, etc.)

## 🧾 Receipt Information

Each order receipt includes:
- ✅ Unique Order ID
- ✅ Table Number
- ✅ Date & Time
- ✅ Customer Details
- ✅ Itemized Order List
- ✅ Total Amount
- ✅ Payment Method & Status
- ✅ Print functionality

## 📧 Email Configuration - SEND REAL EMAILS!

**The system is NOW configured to send REAL emails!**

### Quick Setup (3 Steps):

1. **Enable 2-Factor Authentication on Gmail:**
   - Go to: https://myaccount.google.com/security
   - Enable 2-Step Verification

2. **Generate App Password:**
   - Go to: https://myaccount.google.com/apppasswords
   - Create password for "Mail" → "Restaurant Website"
   - Copy the 16-character password

3. **Update Settings:**
   - Open `restaurant_site/settings.py`
   - Find line ~135:
   ```python
   EMAIL_HOST_USER = 'your-email@gmail.com'      # Your Gmail
   EMAIL_HOST_PASSWORD = 'your-app-password'     # App Password
   ```
   - Replace with YOUR credentials
   - Restart server

**📚 Detailed Guide:** See `EMAIL_SETUP_GUIDE.md` or `SEND_REAL_EMAILS.txt`

**What Customers Receive:**
- ✉️ Reservation confirmation with table number
- ✉️ Order confirmation with Order ID and items
- ✉️ Sent instantly to their email address

## 📱 SMS Notifications

Currently, SMS notifications are simulated through email. To enable real SMS:
1. Integrate with Twilio, AWS SNS, or similar service
2. Add SMS sending function in `views.py`
3. Configure API credentials in settings

## 🗂️ Project Structure

```
restaurant_site/
├── restaurant/              # Main app
│   ├── models.py           # Database models (Menu, Order, Reservation)
│   ├── views.py            # View functions (ordering, cart, payment)
│   ├── admin.py            # Admin panel configuration
│   ├── urls.py             # URL routing
│   ├── templates/          # HTML templates
│   └── management/         # Custom commands
├── restaurant_site/        # Project settings
├── media/                  # Uploaded images
├── static/                 # Static files
└── manage.py              # Django management script
```

## 🎨 Pages Overview

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Landing page with features and featured items |
| Menu | `/menu/` | Complete menu by categories |
| Order Food | `/order/` | Browse and add items to cart |
| Cart | `/cart/` | View and manage cart items |
| Checkout | `/checkout/` | Enter details and payment method |
| Receipt | `/receipt/<order_id>/` | Order confirmation and receipt |
| Book Table | `/reservations/` | Table reservation form |
| About | `/about/` | Restaurant information |
| Contact | `/contact/` | Contact form |
| Admin | `/admin/` | Admin panel |

## 🔧 Management Commands

**Populate sample menu data:**
```bash
python manage.py populate_menu
```

## 📊 Database Models

- **Category** - Menu categories
- **MenuItem** - Individual menu items with prices
- **Order** - Customer orders with payment info
- **OrderItem** - Items in each order
- **Reservation** - Table bookings
- **Contact** - Customer inquiries
- **About** - Restaurant information

## 🎯 Key Features Explained

### Shopping Cart
- Session-based cart (no login required)
- Add/remove items
- Update quantities
- Real-time total calculation
- Persistent across pages

### Order Processing
1. Customer adds items to cart
2. Proceeds to checkout
3. Enters details and table number
4. Selects payment method
5. Order is created with unique ID
6. Receipt is generated
7. Email confirmation sent
8. Cart is cleared

### Reservation Flow
1. Customer fills reservation form
2. System assigns table number
3. Reservation is saved
4. Email sent with confirmation
5. SMS notification (simulated)
6. Admin can manage in panel

## 🔐 Security Notes

- CSRF protection enabled
- SQL injection protection (Django ORM)
- XSS protection
- Secure password hashing
- Session security

## 🚀 Future Enhancements

- User authentication and order history
- Real-time order tracking
- Online payment gateway integration (Stripe, PayPal)
- Real SMS integration
- Loyalty points system
- Reviews and ratings
- Multi-language support
- Mobile app

## 📝 License

This project is for educational purposes.

## 🤝 Support

For issues or questions, use the contact form on the website or check the admin panel for customer inquiries.

---

**Enjoy your restaurant management system! 🍽️**


Add Mail System for Table Booking
Steps to Complete
 Analyze existing code and confirm mail system is already implemented in reservations view
 Update restaurant_site/settings.py with clear email configuration instructions
 User configures real Gmail credentials in settings.py (EMAIL_HOST_USER and EMAIL_HOST_PASSWORD)
 Test the reservation form by submitting a booking to verify email is sent
 Troubleshoot any SMTP errors if emails fail to send
Changes Made
Updated settings.py with detailed instructions for Gmail App Password setup
Switched to console email backend for testing
Notes
The mail system for table booking is already coded in views.py; only configuration is needed.
Ensure Gmail App Password is used for EMAIL_HOST_PASSWORD, not regular password.
Testing completed: Reservation created and email sent to console successfully.
