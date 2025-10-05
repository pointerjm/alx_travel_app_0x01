#!/usr/bin/env python3
"""Serializers for the listings app."""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Listing, Booking


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ListingSerializer(serializers.ModelSerializer):
    """Serializer for Listing model."""
    owner = UserSerializer(read_only=True)
    title = serializers.CharField()

    class Meta:
        model = Listing
        fields = ['listing_id', 'title', 'description', 'price_per_night', 'owner', 'created_at', 'updated_at']

    def validate_title(self, value):
        """Validate title is not empty."""
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model."""
    listing = ListingSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['booking_id', 'listing', 'user', 'start_date', 'end_date', 'total_price', 'created_at']

    def validate(self, data):
        """Validate booking dates."""
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data