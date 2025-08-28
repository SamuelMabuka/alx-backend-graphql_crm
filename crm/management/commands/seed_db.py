from django.core.management.base import BaseCommand
from crm.models import Customer, Product, Order
from django.utils import timezone

class Command(BaseCommand):
    help = "Seeds the database with initial CRM data"

    def handle(self, *args, **options):
        # Seed customers if none exist
        if not Customer.objects.exists():
            Customer.objects.create(name="Sally Thomas", email="sally.thomas@acme.com", phone="123-456-7890")
            Customer.objects.create(name="George Bailey", email="gbailey@foobar.com", phone="987-654-3210")
            Customer.objects.create(name="Edward Walker", email="ed@walker.com")
            self.stdout.write(self.style.SUCCESS("Customers seeded successfully!"))
        else:
            self.stdout.write(self.style.WARNING("Customers already exist."))

        # Optionally, you can also seed Products or Orders here if needed
