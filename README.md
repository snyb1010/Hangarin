# PSUSphere

A web-based Student Organization Management System built with Django, designed to help Palawan State University (PSU) manage student organizations, members, programs, and colleges in one centralized platform.

---

## Short Description

PSUSphere is a Django-powered web application that streamlines the administration of student organizations at PSU. It provides a structured way to manage academic colleges, degree programs, student records, organizations, and organization memberships — making it easy for administrators to track and maintain student involvement across campus.

---

## Features

- **College Management** – Add, update, and manage the list of colleges within the university.
- **Program Management** – Manage degree programs and associate them with their respective colleges.
- **Student Records** – Maintain student profiles including student ID, name, and enrolled program.
- **Organization Management** – Create and manage student organizations with descriptions and college affiliations.
- **Organization Membership Tracking** – Record and monitor which students belong to which organizations, including their date joined.
- **Django Admin Interface** – Full CRUD operations with search, filtering, and list display via Django's built-in admin panel.
- **Timestamps** – Automatic `created_at` and `updated_at` tracking on all records.

---

## Tech Stack

| Technology | Version |
|------------|---------|
| Python     | 3.x     |
| Django     | 6.0.2   |
| SQLite     | (default Django DB) |
| Faker      | 40.5.1  |
| sqlparse   | 0.5.5   |
| asgiref    | 3.11.1  |

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
