# PSUSphere

A web-based Student Organization Management System built with Django, designed to help Palawan State University (PSU) manage student organizations, members, programs, and colleges in one centralized platform.

---

## Short Description

PSUSphere is a Django-powered web application that streamlines the administration of student organizations at PSU. It provides a structured way to manage academic colleges, degree programs, student records, organizations, and organization memberships — making it easy for administrators to track and maintain student involvement across campus.

---

## Features

- **College Management** – List, add, edit, and delete colleges within the university.
- **Program Management** – List, add, edit, and delete degree programs linked to colleges.
- **Student Records** – List, add, edit, and delete student profiles including student ID, name, and enrolled program.
- **Organization Management** – List, add, edit, and delete student organizations with college affiliations.
- **Organization Membership Tracking** – List, add, edit, and delete organization memberships including date joined.
- **Web-Based CRUD Views** – Full ListView, CreateView, UpdateView, and DeleteView for all models via a responsive dashboard UI.
- **Sidebar Navigation** – Quick access to Organization, Org. Members, Student, College, and Program pages.
- **Pagination** – All list views are paginated (5 records per page).
- **Django Admin Interface** – Full CRUD operations with search, filtering, and list display via Django's built-in admin panel.
- **Timestamps** – Automatic `created_at` and `updated_at` tracking on all records.

---

## Tech Stack

| Technology           | Version |
|----------------------|---------|
| Python               | 3.x     |
| Django               | 6.0.2   |
| SQLite               | (default Django DB) |
| django-widget-tweaks | 1.5.1   |
| Faker                | 40.5.1  |
| sqlparse             | 0.5.5   |
| asgiref              | 3.11.1  |
| tzdata               | 2025.3  |

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Rivera-Estoya-PSUSphere
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv psusenv
   # Windows
   psusenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```bash
   cd projectsite
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the admin panel**
   Open your browser and go to: `http://127.0.0.1:8000/admin`

---

## Authors

- **Rivera, Vince Alshie**
- **Estoya, Ethan Laureen**
