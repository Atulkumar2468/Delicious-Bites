from django.core.management.base import BaseCommand
from restaurant.models import Category, MenuItem, About

class Command(BaseCommand):
    help = 'Populate the database with sample menu items'

    def handle(self, *args, **kwargs):
        # Create categories
        appetizers = Category.objects.get_or_create(
            name='Appetizers',
            defaults={'description': 'Start your meal with our delicious starters'}
        )[0]
        
        main_courses = Category.objects.get_or_create(
            name='Main Courses',
            defaults={'description': 'Our signature main dishes'}
        )[0]
        
        desserts = Category.objects.get_or_create(
            name='Desserts',
            defaults={'description': 'Sweet endings to your perfect meal'}
        )[0]
        
        beverages = Category.objects.get_or_create(
            name='Beverages',
            defaults={'description': 'Refreshing drinks to complement your meal'}
        )[0]

        # Create menu items
        menu_items = [
            # Appetizers
            {
                'name': 'Bruschetta',
                'description': 'Toasted bread topped with fresh tomatoes, garlic, basil, and olive oil',
                'price': 8.99,
                'category': appetizers
            },
            {
                'name': 'Mozzarella Sticks',
                'description': 'Crispy fried mozzarella served with marinara sauce',
                'price': 9.99,
                'category': appetizers
            },
            {
                'name': 'Caesar Salad',
                'description': 'Fresh romaine lettuce with parmesan cheese and croutons',
                'price': 10.99,
                'category': appetizers
            },
            {
                'name': 'Chicken Wings',
                'description': 'Spicy buffalo wings served with blue cheese dip',
                'price': 12.99,
                'category': appetizers
            },
            
            # Main Courses
            {
                'name': 'Grilled Salmon',
                'description': 'Fresh Atlantic salmon with lemon butter sauce, served with vegetables',
                'price': 24.99,
                'category': main_courses
            },
            {
                'name': 'Ribeye Steak',
                'description': 'Premium 12oz ribeye steak cooked to perfection with garlic butter',
                'price': 32.99,
                'category': main_courses
            },
            {
                'name': 'Chicken Parmesan',
                'description': 'Breaded chicken breast with marinara sauce and melted mozzarella',
                'price': 18.99,
                'category': main_courses
            },
            {
                'name': 'Pasta Carbonara',
                'description': 'Creamy pasta with bacon, eggs, and parmesan cheese',
                'price': 16.99,
                'category': main_courses
            },
            {
                'name': 'Vegetable Stir Fry',
                'description': 'Fresh seasonal vegetables in a savory Asian sauce',
                'price': 14.99,
                'category': main_courses
            },
            {
                'name': 'Margherita Pizza',
                'description': 'Classic pizza with tomato sauce, mozzarella, and fresh basil',
                'price': 15.99,
                'category': main_courses
            },
            
            # Desserts
            {
                'name': 'Tiramisu',
                'description': 'Classic Italian dessert with coffee-soaked ladyfingers and mascarpone',
                'price': 8.99,
                'category': desserts
            },
            {
                'name': 'Chocolate Lava Cake',
                'description': 'Warm chocolate cake with a molten center, served with vanilla ice cream',
                'price': 9.99,
                'category': desserts
            },
            {
                'name': 'Cheesecake',
                'description': 'New York style cheesecake with berry compote',
                'price': 8.99,
                'category': desserts
            },
            {
                'name': 'Crème Brûlée',
                'description': 'Rich custard topped with caramelized sugar',
                'price': 9.99,
                'category': desserts
            },
            
            # Beverages
            {
                'name': 'Fresh Lemonade',
                'description': 'Homemade lemonade with fresh lemons',
                'price': 4.99,
                'category': beverages
            },
            {
                'name': 'Iced Tea',
                'description': 'Refreshing iced tea with lemon',
                'price': 3.99,
                'category': beverages
            },
            {
                'name': 'Cappuccino',
                'description': 'Italian espresso with steamed milk foam',
                'price': 5.99,
                'category': beverages
            },
            {
                'name': 'Fresh Orange Juice',
                'description': 'Freshly squeezed orange juice',
                'price': 5.99,
                'category': beverages
            },
        ]

        for item_data in menu_items:
            MenuItem.objects.get_or_create(
                name=item_data['name'],
                defaults=item_data
            )

        # Create About content
        About.objects.get_or_create(
            title='Our Story',
            defaults={
                'content': '''Welcome to Delicious Bites, where culinary passion meets exceptional service. 
                
Since 2008, we have been serving our community with the finest dishes prepared by our expert chefs. Our restaurant combines traditional recipes with modern culinary techniques to create unforgettable dining experiences.

We believe in using only the freshest, locally-sourced ingredients to ensure every dish is of the highest quality. Our menu features a diverse selection of appetizers, main courses, desserts, and beverages to satisfy every palate.

Whether you're celebrating a special occasion or simply enjoying a meal with loved ones, our warm and inviting atmosphere provides the perfect setting. Our dedicated staff is committed to making your visit memorable.

Join us and discover why we're the neighborhood's favorite dining destination!'''
            }
        )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample menu items!'))
