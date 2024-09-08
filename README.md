# Django Invoicing Application

## Overview

This is a simple invoicing application built with Django, HTML, CSS, and JavaScript. The application allows users to create, view, edit, and manage invoices with multiple items and associated taxes.

## Features

- Create new invoices with multiple items
- Add and manage various taxes for each item
- Edit existing invoices and items
- View detailed invoices with item breakdowns and total calculations
- Automatically calculate and display tax amounts for each item

### Setup Instructions

1. **Clone the repository:**

   ```bash
   cd invoicing_app

2. Create a virtual environment (optional but recommended):

  ```bash
  python -m venv env
  source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. Install Dependencies
```
pip install -r requirements.txt
```
4. Add migrations
```
python manage.py migrate
```
5. Apply Migrations
```
python manage.py migrate
```
6. Run the server
```
python manage.py runserver
```
