# Mobile Shop Backend

A Django REST Framework API for managing mobile phone brands, suppliers, models, stock items, and sales.

## Stack

- Python
- Django 6.1
- Django REST Framework
- SQLite

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the dependencies:

   ```powershell
   pip install django djangorestframework
   ```

3. Apply database migrations:

   ```powershell
   python manage.py migrate
   ```

4. Start the development server:

   ```powershell
   python manage.py runserver
   ```

The API is available at `http://127.0.0.1:8000/api/shop/`.

## API Endpoints

All resources support the standard Django REST Framework `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` operations.

| Resource      | Endpoint               |
| ------------- | ---------------------- |
| Brands        | `/api/shop/brands/`    |
| Suppliers     | `/api/shop/suppliers/` |
| Mobile models | `/api/shop/models/`    |
| Stock items   | `/api/shop/stock/`     |
| Sales         | `/api/shop/sales/`     |

Detail endpoints use the resource ID, for example `/api/shop/brands/1/`.

## Data Model

- **Brand**: Unique brand name.
- **Supplier**: Name, optional address, and optional phone number.
- **Mobile model**: Model name, base price, selling price, brand, and optional supplier.
- **Stock item**: Unique 15-character IMEI, mobile model, and status.
- **Sale**: Stock item, customer name, sale price, and sale date.

Stock statuses are `Available`, `Sold`, and `Defective`.

## Sales Rules

When a sale is created:

- The stock item must have status `Available`.
- Sold or defective phones cannot be sold.
- The stock item is automatically changed to `Sold` after the sale is created.

## Example Requests

Create a brand:

```http
POST /api/shop/brands/
Content-Type: application/json

{
  "name": "Example Mobile"
}
```

Create a stock item:

```http
POST /api/shop/stock/
Content-Type: application/json

{
  "imei": "123456789012345",
  "status": "Available",
  "mobile_model": 1
}
```

Create a sale:

```http
POST /api/shop/sales/
Content-Type: application/json

{
  "stock_item": 1,
  "customer_name": "Jane Doe",
  "sale_price": "799.99"
}
```

## Useful Commands

```powershell
# Check the project for configuration issues
python manage.py check

# Create migrations after model changes
python manage.py makemigrations

# Run tests
python manage.py test

# Create an admin user
python manage.py createsuperuser
```

The Django admin is available at `http://127.0.0.1:8000/admin/` when the development server is running.
