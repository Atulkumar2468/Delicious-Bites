import os
import django
from django.test import Client
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_site.settings')
django.setup()

# Create a test client
client = Client()

# Test data for reservation
test_data = {
    'name': 'Test User',
    'email': 'test@example.com',
    'phone': '1234567890',
    'date': '2025-12-01',
    'time': '18:00',
    'guests': 4,
    'special_requests': 'Window seat please'
}

# Make POST request to reservations view
response = client.post('/reservations/', test_data)

print(f"Response status: {response.status_code}")
print(f"Response content: {response.content.decode()}")

# Check if reservation was created
from restaurant.models import Reservation
reservations = Reservation.objects.filter(email='test@example.com')
if reservations.exists():
    print("Reservation created successfully!")
    print(f"Reservation details: {reservations.first()}")
else:
    print("Reservation not created.")
