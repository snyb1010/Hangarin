# PSUSphere

A Django web application for managing student organizations at Palawan State University.

## Description

PSUSphere is a student organization management system built with Django. It provides a dashboard to track colleges, programs, students, organizations, and organization memberships. The app includes search, sorting, and social login features.

## Features

- **Dashboard** — Summary cards showing total students, students who joined this year, total organizations, and total programs
- **Colleges** — View and search colleges
- **Programs** — View, search, and sort programs by name or college
- **Students** — View and search students by name
- **Organizations** — View and search organizations, sorted by college and name
- **Org Members** — View, search, and sort members by student name or date joined
- **Authentication** — Login/logout with username or email; Social login via Google and GitHub (django-allauth)
- **Django Admin** — Full backend management panel
- **Pagination** — All list pages are paginated

## Tech Stack

- Python 3.12
- Django 6.0.2
- SQLite
- django-allauth 65.x (Google & GitHub OAuth)
- django-widget-tweaks
- Faker (for seed data)

## How to Run

```bash
# Activate virtual environment (Windows)
psusenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
cd projectsite
python manage.py migrate

# (Optional) Create a superuser for admin access
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Then open your browser and go to `http://127.0.0.1:8000/`

## Social Login Setup (Google & GitHub)

To enable Google and GitHub login, add your OAuth credentials to `projectsite/settings.py`:

```python
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '<your-google-client-id>',
            'secret': '<your-google-client-secret>',
            'key': ''
        }
    },
    'github': {
        'APP': {
            'client_id': '<your-github-client-id>',
            'secret': '<your-github-client-secret>',
            'key': ''
        }
    }
}
```

- **Google**: Create credentials at [console.cloud.google.com](https://console.cloud.google.com/) — set redirect URI to `http://127.0.0.1:8000/accounts/google/login/callback/`
- **GitHub**: Create an OAuth App at [github.com/settings/developers](https://github.com/settings/developers) — set callback URL to `http://127.0.0.1:8000/accounts/github/login/callback/`

## Authors

- Rivera, Vince Alshie
- Estoya, Ethan Laureen
