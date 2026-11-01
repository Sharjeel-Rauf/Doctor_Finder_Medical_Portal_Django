
# Doctor Finder – Medical Portal

This README provides an overview of the structure and features of a Django medical portal that helps patients find doctors.



## Overview
Developed a Django web application that connects patients with doctors. It uses a custom user model with patient and doctor roles, and gives patients one search box to find doctors by name, speciality or hospital.



## Technologies Used
* **Django** - Web framework
* **SQLite** - Database
* **Custom User Model** - `AbstractUser` with patient and doctor roles
* **HTML, CSS** - Front-end templates

## Features
* **Custom User Model**: A single `User` model with `is_patient` and `is_doctor` roles, linked to separate patient and doctor profiles.
* **Patient Profiles**: Name, phone number, age, gender, date of birth and blood group.
* **Doctor Profiles**: Name, phone number, speciality and hospital.
* **Login and Logout**: Session-based authentication with success and error messages.
* **Patient Interface**: Lists all registered doctors.
* **Doctor Search**: Finds doctors by name, speciality or hospital using Django `Q` objects.
* **Admin Panel**: Patients and doctors are managed from the Django admin.

## Status
* The patient and doctor sign-up pages are still in progress. For now, create accounts and doctor profiles from the Django admin panel.

## Files
* **`medicine_django/medicine_app/`**: Custom user, patient and doctor models, the patient interface and doctor search.
* **`medicine_django/member/`**: Login, logout and sign-up forms.
* **`medicine_django/templates/base.html`**: Base template shared by all pages.

## How to use
1. **Clone the repository**: Clone the project repository to your local machine.
    ```bash
    git clone https://github.com/Sharjeel-Rauf/Doctor_Finder_Medical_Portal_Django.git
    cd Doctor_Finder_Medical_Portal_Django
    ```
2. **Set up a virtual environment**: Create a virtual environment and activate it.
    ```bash
    python -m venv venv
    venv\Scripts\activate        # Windows
    source venv/bin/activate     # macOS / Linux
    ```
3. **Install dependencies**: Install dependencies from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply migrations**: Create the necessary database tables.
    ```bash
    cd medicine_django
    python manage.py migrate
    ```
5. **Create an admin account**: Use it to add patients and doctors at `http://localhost:8000/admin/`.
    ```bash
    python manage.py createsuperuser
    ```
6. **Run the server**: Start the development server.
    ```bash
    python manage.py runserver
    ```
7. **Access the app**: Open a web browser and navigate to `http://localhost:8000/` to interact with the app.

## App Usage

- **Add doctors**: Sign in to the admin panel and add doctor profiles.
- **Log in**: Use the login page to sign in.
- **Browse doctors**: The patient interface lists all registered doctors.
- **Search**: Type a name, speciality or hospital to find matching doctors.

## Contributing

* Contributions are welcome! Feel free to fork the repository and submit a pull request for any improvements.
