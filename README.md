# E-Commerce for Texas State University
I developed a Django-based e-commerce platform as part of a course project, enabling users(students) to browse products, manage carts, place orders, provide feedback, engage in chat, and express preferences through likes/dislikes. The application includes user authentication, administrative controls, product recommendations, and order tracking features.

## Features

- Admin panel for managing products and users
- User product browsing
- Prediction and random product generation modules
- Simple date handling with `Dates.py`

## STEPS

1. Clone or download the repository
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

5. Access the app at `http://127.0.0.1:8000/`


## Tech Stack

Python

Django 2.2

MySQL
