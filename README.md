# Student Placement Tracker

A web-based application built with Django to help students manage and track their job and internship applications in one place.

## 🌐 Live Demo

**Live Website:** https://student-placement-tracker-ciiz.onrender.com

## 📌 Project Overview

The Student Placement Tracker helps students organize their placement preparation and keep track of job and internship opportunities. Students can create an account, manage their profile, browse job listings, and record their application progress.

## ✨ Features

* **Student Registration:** Create a student account.
* **Login and Logout:** Secure account authentication using Django.
* **Student Profile:** View and update profile information.
* **Job Listings:** Browse available job opportunities.
* **Application Management:** Track job and internship applications.
* **Edit Opportunities:** Update saved application details.
* **Responsive Interface:** Access the website on desktop and mobile devices.

## 🛠️ Technologies Used

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap 5
* **Database:** SQLite
* **Deployment:** Render
* **Version Control:** Git and GitHub

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/amaltomyy/student-placement-tracker.git
cd student-placement-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## 📂 Project Structure

```text
student-placement-tracker/
├── config/
├── placement/
│   ├── migrations/
│   ├── templates/
│   │   └── placement/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
```

## 🎯 Project Objective

The main objective of this project is to provide students with a simple platform to organize job opportunities and monitor their placement application progress.

## 👨‍💻 Developer

**Amal Tomy**

GitHub: https://github.com/amaltomyy

LinkedIn: https://linkedin.com/in/amal-t-tomy

## 📄 License

This project was developed for educational and portfolio purposes.
