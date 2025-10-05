alx_travel_app_0x01
Overview
The alx_travel_app_0x01 project is a Django-based RESTful API for managing travel listings and bookings, built using Django REST Framework (DRF). It provides CRUD (Create, Read, Update, Delete) operations for Listing and Booking models, following RESTful conventions. The API endpoints are accessible under /api/ and are designed to be scalable, secure, and testable. This project is a continuation of alx_travel_app_0x00, enhanced with API functionality for a travel booking platform similar to Airbnb or Booking.com.
Features

CRUD Operations: Fully functional endpoints for creating, retrieving, updating, and deleting listings and bookings.
RESTful Design: Endpoints follow REST conventions, e.g., /api/listings/ and /api/bookings/.
Authentication and Authorization: Requires user authentication for all actions, with permission checks to ensure only owners or admins can modify/delete resources.
Automatic URL Routing: Uses DRF’s DefaultRouter for clean, maintainable URL configurations.
Testing: Endpoints are tested with Postman to ensure reliability and correct error handling.
Future Swagger Integration: Planned support for interactive API documentation using drf-yasg.

Setup Instructions

Clone the Repository:
git clone https://github.com/your-username/alx_travel_app_0x01.git
cd alx_travel_app


Install Dependencies:Ensure Python

