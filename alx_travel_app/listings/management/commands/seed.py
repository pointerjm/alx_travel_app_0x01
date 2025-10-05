#!/usr/bin/env python3
"""Management command to seed the database with sample listings data."""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
import uuid


class Command(BaseCommand):
    """Command to seed listings data."""
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **options):
        """Execute the seeding process."""
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        # Create sample users
        users = [
            {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'},
            {'username': 'user2', 'email': 'user2@example.com', 'password': 'password123'},
        ]
        for user_data in users:
            User.objects.get_or_create(
                username=user_data['username'],
                defaults={'email': user_data['email'], 'password': user_data['password']}
            )

        # Create sample listings
        listings = [
            {
                'listing_id': uuid.uuid4(),
                'title': 'Cozy Beach House',
                'description': 'A beautiful beach house with ocean views.',
                'price_per_night': 150.00,
                'owner': User.objects.get(username='user1'),
            },
            {
                'listing_id': uuid.uuid4(),
                'title': 'Mountain Cabin',
                'description': 'A rustic cabin in the mountains.',
                'price_per_night': 100.00,
                'owner': User.objects.get(username='user2'),
            },
        ]

        for listing_data in listings:
            Listing.objects.get_or_create(
                listing_id=listing_data['listing_id'],
                defaults={
                    'title': listing_data['title'],
                    'description': listing_data['description'],
                    'price_per_night': listing_data['price_per_night'],
                    'owner': listing_data['owner'],
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with listings.'))