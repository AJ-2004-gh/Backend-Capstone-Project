# 🍽️ Little Lemon - Restaurant Menu API

This backend project is developed as part of the **Meta Back-End Developer Certificate Program**. It provides a **RESTful API** for managing and viewing restaurant menu items and booking tables. The project uses **Django**, **Django REST Framework**, and **Djoser** for user authentication.

---

## 📌 Features

- ✅ **Django-based** backend architecture
- ✅ REST API endpoints for:
  - Viewing and managing menu items
  - Booking table reservations
  - User authentication (login/logout/token management)
- ✅ **Authentication** using **Djoser + DRF Token Authentication**
- ✅ **Admin panel** for managing menu and bookings
- ✅ Modular, scalable, and clean project structure
- ✅ **Unit & view tests** for model and endpoint validation

---

## 🛠️ Tech Stack

| Tech           | Usage                         |
|----------------|-------------------------------|
| Python 3.x     | Programming Language          |
| Django         | Web framework                 |
| Django REST Framework | API development        |
| Djoser         | Authentication token management |
| Mysql         | Default database (can be swapped) |
| Insomnia        | API testing (optional)        |
| VS Code        | Development Environment       |

---

## 🧩 Project Structure

```bash
LittleLemon/
│
├── littlelemon/             # Project package
│   └── settings.py
│   └── urls.py
│   └── ...
│
├── restaurant/              # App package
│   ├── models.py            # Menu and Booking models
│   ├── views.py             # API views
│   ├── serializers.py       # DRF serializers
│   ├── urls.py              # App-level routing
│   └── tests/               # Test folder for models and views
│       ├── test_models.py
│       └── test_views.py
│
├── templates/               # HTML templates
│   └── index.html
│
├── static/                  # Static assets
│   └── restaurant/
│       └── img/
│           └── logo.png
│           └── grill.jpg
│           └── ...
│
└── manage.py
