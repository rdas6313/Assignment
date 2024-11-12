
# Invoice Management API

This project provides a simple REST API for managing invoices. You can create, retrieve, and update invoices using Django and Django REST Framework.


## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Apply migrations:
```bash
python manage.py migrate
```
Run the development server:
```bash
python manage.py runserver
```

The API should now be accessible at http://127.0.0.1:8000/.
## Assumptions
Assume that a POST request will be made to /api/invoices, and PUT and GET requests to retrieve or update a specific invoice will be made to the /api/invoices/<invoice_number>/ endpoint.
Request body and response demo:

```bash
{
    "invoice_number": "in0012",
    "customer_name": "Rahul Sharma",
    "date": "2022-12-01",
    "details": [
        {
            "description": "Product B",
            "quantity": 2,
            "price": "75.00",
            "line_total": "150.00"
        }
    ]
}
```
