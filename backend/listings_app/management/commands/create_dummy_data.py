import random
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker
from listings_app.models import Category, Listing, User, Image

fake = Faker()

User = get_user_model()

class Command(BaseCommand):
    help = 'Generate dummy data for users, categories, and listings'

    def handle(self, *args, **kwargs):

        self.stdout.write(self.style.SUCCESS('Creating categories'))
        self.create_categories()
        #self.stdout.write(self.style.SUCCESS('Creating users'))
        #self.create_dummy_users()

        

        #self.stdout.write(self.style.SUCCESS('Creating dummy listings...'))
        #self.create_dummy_listings()

    def create_dummy_users(self, total_users=100):
        User.create_super_user(username="noel", email="noel.klp@gmail.com", password="deXSA1234", bio="Interested in learning new stuff.")

        for _ in range(total_users):
            username = fake.user_name()
            email = fake.email()
            password = fake.password()
            bio = fake.text(max_nb_chars=100)

            if not User.objects.filter(email=email).exists():
                User.create_user(username=username, email=email, password=password, bio=bio)

    def create_categories(self):
        categories = [
            {'category_name': 'builds', 'description': 'Guides and tutorials for creating and assembling various projects.'},
            {'category_name': 'resources', 'description': 'Collections of tools, materials, and references useful for building projects.'},
            {'category_name': 'projects', 'description': 'Showcases and details about completed or ongoing creative endeavors.'},
            {'category_name': 'documents', 'description': 'Documentation and written materials related to project planning and execution.'}
        ]
        for category in categories:
            Category.objects.create(name=category['category_name'], description=category['description'])

    def create_dummy_listings(self, total_listings=5200):
        users = User.objects.all()
        categories = Category.objects.all()

        for _ in range(total_listings):
            title = fake.sentence()
            text = fake.paragraph()
            owner = random.choice(users)
            category = random.choice(categories)

            listing = Listing.create_listing(title=title, text=text, owner=owner, category=category)
            Image.objects.create(listing=listing,src='default.png')

        self.stdout.write(self.style.SUCCESS('Dummy data generation complete.'))