# 🎓 Student Course Management API

A simple **backend-only REST API** built with **Django REST Framework** for managing students, courses, and enrollments.

## ✨ Features

* 👨‍🎓 Student CRUD
* 📚 Course CRUD
* 📝 Course enrollment
* 🔐 Custom permissions
* 🔎 Search & filtering
* 📄 Pagination
* 🛡️ Data validation
* ⚙️ Django Admin

## 🔗 Models

```text
Student ────< Enrollment >──── Course
```

* **Student** → Student information
* **Course** → Course details & fees
* **Enrollment** → Connects students with courses

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

## 🚀 Run Locally

```bash
git clone <your-repository-url>
cd Student-Course-Management-API

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

## 🎯 Purpose

Built as a **DRF learning project** to practice building real-world REST APIs and understand permissions, relationships, CRUD, filtering, and pagination.

---

### 👨‍💻 Author

**Mahesh Raj Lamsal**

⭐ *Learning. Building. Improving.*
