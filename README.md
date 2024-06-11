# Acme Corp Product API

Acme Corp Product API is a Django-based RESTful API for managing products. This project is part of a test assignment for an intern position at Acme Corp. The API allows users to create, retrieve, filter, and sort products.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/AcmeCorp.git
   cd AcmeCorp
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
## API Endpoints

- Create a new product
  
  `POST /api/products/`
  
- Get a list of products
  
  `GET /api/products/`
  
- Get product by ID
  
  `GET /api/products/<id>/`
  
- Get sorted product
  
  `GET /api/products?sort=price`
  
- Get product by category
  
  `GET /api/products?category=Example%20Category`

  
