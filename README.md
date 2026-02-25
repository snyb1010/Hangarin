# PSUSphere

A Django web app for managing student organizations at Palawan State University.

## Description

PSUSphere lets you manage colleges, programs, students, organizations, and org memberships through a simple dashboard. Built as a school project using Django.

## Features

- Manage Colleges, Programs, Students, Organizations, and Org Members
- Add, edit, and delete records from the web interface
- Django admin panel for backend management
- Pagination on all list pages

## Tech Stack

- Python
- Django 6.0.2
- SQLite
- django-widget-tweaks

## How to Run

```bash
# Activate virtual environment
psusenv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Run migrations
cd projectsite
python manage.py migrate

# Start server
python manage.py runserver
```

Then go to `http://127.0.0.1:8000/`

## Authors

- Rivera, Vince Alshie
- Estoya, Ethan Laureen
