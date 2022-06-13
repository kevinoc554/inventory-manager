# README
The Inventory Manager is an inventory tracking web application for a logistics company. The application allows users to add, view, edit and delete items in the inventory, along with the ability to undelete items and leave deletion comments.

This project was completed as part of the Fall 2022 - Shopify Developer Intern Challenge.

## Technologies
Languages:
- Python
- HTML

Frameworks/Libraries:
- Django

Database:
- SQLite

## Features
The site offers the following functionality:
- Create:
    - Users can create new inventory items
- Read:
    - Users can read the contents of the database on a table on the home page
- Update:
    - Users can update existing database entries on the Edit page
- Delete:
    - Users can delete items, removing them from the table of currently available items. Users can also leave a deletion comment
- Undelete:
    - Users can restore deleted items. This will return them to the table of available items, and remove any deletion comments.

## Deployment
### Local:
To run the application locally:
1. Clone the repository using ``git clone https://github.com/kevinoc554/inventory-manager.git``.
2. Install the required packages using ``pip install -r requirements.txt``.
3. Run the server using ``python manage.py runserver``.

### Replit:
To run the app on Replit:
1. Navigate to the [Repl](https://replit.com/@kevinoc/inventory-manager).
2. Fork the Repl, using the button the top right.
3. Install the required packages using ``pip install -r requirements.txt``.
4. Run the server using ``python manage.py runserver``.
