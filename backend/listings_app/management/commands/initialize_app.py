from django.core.management.base import BaseCommand
from listings_app.models import Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating categories'))
        self.create_categories()

    def create_categories(self):
        categories = [
            {'category_name': 'builds', 'description': 'Guides and tutorials for creating and assembling various projects.'},
            {'category_name': 'resources', 'description': 'Collections of tools, materials, and references useful for building projects.'},
            {'category_name': 'projects', 'description': 'Showcases and details about completed or ongoing creative endeavors.'},
            {'category_name': 'documents', 'description': 'Documentation and written materials related to project planning and execution.'}
        ]

        if not Category.objects.exists():
            for category in categories:
                Category.objects.create(name=category['category_name'], description=category['description'])
        else:
            self.stdout.write(self.style.WARNING('Categories have already been create, skipping creation.'))
