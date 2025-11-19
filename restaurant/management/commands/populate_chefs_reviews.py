from django.core.management.base import BaseCommand
from restaurant.models import Chef, Review

class Command(BaseCommand):
    help = 'Populate the database with sample chefs and reviews'

    def handle(self, *args, **kwargs):
        # Create Chefs
        chefs_data = [
            {
                'name': 'Marco Rossi',
                'position': 'Head Chef',
                'bio': 'With over 20 years of experience in Italian cuisine, Chef Marco brings authentic flavors and innovative techniques to every dish. Trained in Rome and Milan, he specializes in traditional pasta and seafood dishes.',
                'experience_years': 20,
                'specialty': 'Italian Cuisine & Pasta',
                'order': 1
            },
            {
                'name': 'Sarah Chen',
                'position': 'Pastry Chef',
                'bio': 'Award-winning pastry chef with a passion for creating exquisite desserts. Sarah combines French techniques with Asian flavors to create unique and memorable sweet experiences.',
                'experience_years': 12,
                'specialty': 'Desserts & Pastries',
                'order': 2
            },
            {
                'name': 'James Anderson',
                'position': 'Sous Chef',
                'bio': 'Specializing in modern American cuisine with a focus on locally-sourced ingredients. James brings creativity and precision to every plate, ensuring exceptional quality and presentation.',
                'experience_years': 15,
                'specialty': 'American Cuisine & Grilling',
                'order': 3
            },
            {
                'name': 'Maria Garcia',
                'position': 'Sushi Chef',
                'bio': 'Master sushi chef trained in Tokyo with expertise in traditional Japanese cuisine. Maria creates beautiful and delicious sushi using the freshest ingredients and time-honored techniques.',
                'experience_years': 18,
                'specialty': 'Japanese Cuisine & Sushi',
                'order': 4
            }
        ]

        for chef_data in chefs_data:
            Chef.objects.get_or_create(
                name=chef_data['name'],
                defaults=chef_data
            )

        # Create Reviews
        reviews_data = [
            {
                'customer_name': 'John Smith',
                'rating': 5,
                'comment': 'Absolutely amazing experience! The food was exceptional, service was impeccable, and the ambiance was perfect. The Grilled Salmon was cooked to perfection. Highly recommend!',
                'is_featured': True
            },
            {
                'customer_name': 'Emily Johnson',
                'rating': 5,
                'comment': 'Best restaurant in town! The pasta carbonara was divine and the tiramisu was the perfect ending. Our server was attentive and knowledgeable. Will definitely be back!',
                'is_featured': True
            },
            {
                'customer_name': 'Michael Brown',
                'rating': 5,
                'comment': 'Outstanding food and service! Every dish we tried was delicious. The ribeye steak was cooked exactly as requested. The atmosphere is elegant yet comfortable.',
                'is_featured': True
            },
            {
                'customer_name': 'Sarah Davis',
                'rating': 4,
                'comment': 'Great dining experience! The menu has wonderful variety and everything we ordered was fresh and flavorful. The staff was friendly and accommodating. Definitely worth a visit!',
                'is_featured': True
            },
            {
                'customer_name': 'David Wilson',
                'rating': 5,
                'comment': 'Incredible meal from start to finish! The bruschetta appetizer was fresh and tasty, and the chicken parmesan was outstanding. The chocolate lava cake was heavenly!',
                'is_featured': True
            },
            {
                'customer_name': 'Jennifer Martinez',
                'rating': 5,
                'comment': 'Perfect place for a special occasion! The food quality is exceptional and the presentation is beautiful. Our chef really knows how to create memorable dishes. Five stars!',
                'is_featured': True
            }
        ]

        for review_data in reviews_data:
            Review.objects.get_or_create(
                customer_name=review_data['customer_name'],
                defaults=review_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated chefs and reviews!'))
