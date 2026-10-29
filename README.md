# StudyMatrix — Student Management System

## Project Overview

StudyMatrix is a web-based Student Management System
developed using Python and Django. It helps administrators
manage student records, track academic performance,
search and filter student information, and export data
to CSV and Excel files.

## Features

- **Dashboard:** View student statistics, average marks, topper information, and course summaries.
- **Student Management:** Add, view, edit, and delete student records.
- **Form Validation:** Validate student information and prevent invalid or duplicate records.
- **Authentication:** Login, logout, and restrict access to protected pages.
- **Search:** Find students by name, roll number, course, or email.
- **Filters:** Filter records by course and marks range.
- **Pagination:** Display student records across multiple pages.
- **Data Export:** Download student records as CSV and Excel files.
- **Responsive Interface:** Bootstrap-based styling for a cleaner user experience.

## Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Data Export:** Python CSV module, OpenPyXL
- **Development Tools:** Visual Studio Code

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Student_Management_System
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Create and activate a virtual environment

```bash
python -m venv myenv
```

Windows Command Prompt:

```bash
myenv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install django openpyxl
```

### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to set your administrator username and password.

### 6. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

`http://127.0.0.1:8000/`

## Project Structure

```text
Student_Management_System/
├── manage.py
├── student_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── students/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── templates/
    │   └── students/
    └── static/
        └── students/
```

## Learning Outcomes

This project demonstrates practical experience with Django application development, database models, form validation, authentication, CRUD operations, query filtering, pagination, dashboard development, and file exports.

## Future Enhancements

- Role-based access for administrators and staff.
- Student profile photographs and document uploads.
- Attendance and examination management.
- Automated testing and improved reporting.
- Deployment to a production hosting platform.

## Security Note

For production deployment, configure environment variables for secrets, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and use a suitable production database and hosting setup. Never commit passwords or secret keys to a public repository.
