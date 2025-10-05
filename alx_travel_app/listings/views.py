# file: listings/views.py

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Listing objects with CRUD operations.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return listings, filtered by owner for non-admin users.
        """
        if self.request.user.is_staff:
            return Listing.objects.all()
        return Listing.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the owner to the authenticated user.
        """
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        """
        Ensure only the owner or admin can update a listing.
        """
        if self.request.user.is_staff or self.get_object().owner == self.request.user:
            serializer.save()
        else:
            return Response(
                {"detail": "You do not have permission to edit this listing."},
                status=status.HTTP_403_FORBIDDEN
            )

    def perform_destroy(self, instance):
        """
        Ensure only the owner or admin can delete a listing.
        """
        if self.request.user.is_staff or instance.owner == self.request.user:
            instance.delete()
        else:
            return Response(
                {"detail": "You do not have permission to delete this listing."},
                status=status.HTTP_403_FORBIDDEN
            )


class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Booking objects with CRUD operations.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return bookings, filtered by user for non-admin users.
        """
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Automatically set the user to the authenticated user and calculate total_price.
        """
        listing = serializer.validated_data['listing']
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        
        # Calculate total_price based on nights
        nights = (end_date - start_date).days
        if nights <= 0:
            return Response(
                {"detail": "End date must be after start date."},
                status=status.HTTP_400_BAD_REQUEST
            )
        total_price = nights * listing.price_per_night
        
        serializer.save(user=self.request.user, total_price=total_price)

    def perform_update(self, serializer):
        """
        Ensure only the user who made the booking or admin can update it.
        """
        booking = self.get_object()
        if self.request.user.is_staff or booking.user == self.request.user:
            listing = serializer.validated_data.get('listing', booking.listing)
            start_date = serializer.validated_data.get('start_date', booking.start_date)
            end_date = serializer.validated_data.get('end_date', booking.end_date)
            
            # Recalculate total_price if dates or listing change
            nights = (end_date - start_date).days
            if nights <= 0:
                return Response(
                    {"detail": "End date must be after start date."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            total_price = nights * listing.price_per_night
            
            serializer.save(total_price=total_price)
        else:
            return Response(
                {"detail": "You do not have permission to edit this booking."},
                status=status.HTTP_403_FORBIDDEN
            )

    def perform_destroy(self, instance):
        """
        Ensure only the user who made the booking or admin can delete it.
        """
        if self.request.user.is_staff or instance.user == self.request.user:
            instance.delete()
        else:
            return Response(
                {"detail": "You do not have permission to delete this booking."},
                status=status.HTTP_403_FORBIDDEN
            )