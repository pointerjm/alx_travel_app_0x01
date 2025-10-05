ALX Travel App
Description
This project implements a Django-based travel application with database models, serializers, and a management command to seed sample data. It includes Listing, Booking, and Review models for managing travel listings.
Files

alx_travel_app/settings.py: Project configuration with listings app.
listings/models.py: Defines Listing, Booking, and Review models.
listings/serializers.py: Serializers for Listing and Booking models.
listings/management/commands/seed.py: Management command to seed sample listings.
.env: Environment variables (SECRET_KEY, DEBUG).

Setup

Clone the repository:git clone <repository-url>
cd alx_travel_app


Create and activate a virtual environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install django==4.2.16 django-environ


Create .env with SECRET_KEY and DEBUG=True.
Apply migrations:python manage.py makemigrations
python manage.py migrate


Seed the database:python manage.py seed


Create a superuser:python manage.py createsuperuser


Run the server:python manage.py runserver



Author
Julius Maina