
# Doctor Finder – Medical Portal

This README provides an overview of the structure and features of a Django medical portal that helps patients find doctors.



## Overview
Developed a Django web application that connects patients with doctors. It uses a custom user model with patient and doctor roles, lets each sign up with their own profile, and gives patients one search box to find doctors by name, speciality or hospital.



## Technologies Used
* **Django** - Web framework
* **SQLite** - Database
* **Custom User Model** - `AbstractUser` with patient and doctor roles
* **HTML, CSS** - Front-end templates

## Features
* **Custom User Model**: A single `User` model with `is_patient` and `is_doctor` roles, linked to separate patient and doctor profiles.
* **Patient Sign-up**: Patients create an account with their name, phone number, age, gender, date of birth and blood group.
* **Doctor Sign-up**: Doctors create an account with their name, phone number, speciality and hospital, and appear in the doctor list straight away.
* **One-step Registration**: The login account and its profile are saved together in one database transaction, and the new user is logged in automatically.
* **Login and Logout**: Session-based authentication.
* **Patient Interface**: Lists all registered doctors with their contact details.
* **Doctor Search**: Finds doctors by name, speciality or hospital using Django `Q` objects.
* **Admin Panel**: Patients and doctors can also be managed from the Django admin.
* **Automated Tests**: Tests cover patient and doctor sign-up, login and invalid sign-ups.

## Files
* **`medicine_django/medicine_app/`**: Custom user, patient and doctor models, the patient interface and doctor search.
* **`medicine_django/member/`**: Login, logout, patient and doctor sign-up forms, and their tests.
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
5. **Create an admin account (optional)**: Use it to manage patients and doctors at `http://localhost:8000/admin/`.
    ```bash
    python manage.py createsuperuser
    ```
6. **Run the server**: Start the development server.
    ```bash
    python manage.py runserver
    ```
7. **Access the app**: Open a web browser and navigate to `http://localhost:8000/` to interact with the app.
8. **Run the tests**: Check the sign-up and login flows.
    ```bash
    python manage.py test member
    ```

## App Usage

- **Sign up as a doctor**: Click "Are you a Doctor?" on the home page and fill in your profile.
- **Sign up as a patient**: Click "Are you a Patient?", then follow the patient sign-up link under the login form.
- **Log in**: Use the login page to sign in.
- **Browse doctors**: The patient interface lists all registered doctors.
- **Search**: Type a name, speciality or hospital to find matching doctors.

## Contributing

* Contributions are welcome! Feel free to fork the repository and submit a pull request for any improvements.
