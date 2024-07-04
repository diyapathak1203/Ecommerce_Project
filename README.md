# Django eCommerce Web Application

This Django-based eCommerce web application allows users to browse products, add them to a cart, and proceed to checkout. It includes features for user authentication, product management, order processing, and payment integration.

## Features

- Open and browse products
- Add products to cart
- User authentication (login, logout, signup)
- Product management (CRUD operations)
- Order processing
- Payment integration

## Requirements

- Python 3.x
- Django

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/django-ecommerce.git
    cd django-ecommerce
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser (admin account):
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the admin panel at `http://127.0.0.1:8000/admin/` to manage products and view orders.

## Usage

1. Navigate to `http://127.0.0.1:8000/` to view the eCommerce site.
2. Sign up or log in to browse products, add items to the cart, and proceed to checkout.
3. Use the admin panel to manage products, view orders, and update user information.
4. Integrate payment gateways for accepting payments securely.



