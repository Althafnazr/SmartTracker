# ⚡ Smart Electronic Inventory & Service Tracker

A full-stack web application built with **Python** and **Django** for managing electronic spare parts inventory and repair service requests in an electronics shop.

---
## 🚀 Features

- 🔐 **Authentication** — Secure login/logout using Django's built-in auth system
- 👥 **Role-Based Access Control** — Three roles with different permissions
  - **Admin** — Full system access
  - **Shop Staff** — Manage product inventory
  - **Service Staff** — Manage service requests
- 📦 **Product Inventory Management** — Add, edit, delete electronic spare parts
- 🔧 **Service Request Management** — Track repair jobs from received to completed
- 📉 **Auto Stock Deduction** — Stock automatically decreases when a part is used in a service request
- 📊 **Live Dashboard** — Real-time revenue, profit, and service statistics
- ⚠️ **Low Stock Alerts** — Flags products with stock quantity ≤ 2
- 🎨 **Modern Dark UI** — Clean dark theme with Bootstrap and Google Fonts

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, Django 6.0 |
| Database | SQLite |
| Frontend | HTML, CSS, Bootstrap 5 |
| Auth | Django Authentication System |
| Fonts | Space Grotesk, JetBrains Mono |

---

## 📁 Project Structure

```
SmartTracker/
│
├── inventory/
│   ├── migrations/
│   ├── templates/
│   │   ├── inventory/
│   │   │   ├── base.html
│   │   │   ├── dashboard.html
│   │   │   ├── product_list.html
│   │   │   ├── product_form.html
│   │   │   ├── product_delete.html
│   │   │   ├── service_request_list.html
│   │   │   ├── service_request_form.html
│   │   │   └── service_delete.html
│   │   └── registration/
│   │       └── login.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── SmartTracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/SmartTracker.git
cd SmartTracker
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django
```

Or if you have a requirements file:
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Run the development server
```bash
python manage.py runserver
```

Visit 👉 `http://127.0.0.1:8000`

---

## 👥 Setting Up User Roles

After running the server, go to `http://127.0.0.1:8000/admin/`

1. Create three **Groups**: `Admin`, `ShopStaff`, `ServiceStaff`
2. Assign permissions to each group:

| Group | Permissions |
|-------|------------|
| ShopStaff | view, add, change, delete **product** |
| ServiceStaff | view, add, change, delete **servicerequest** |
| Admin | All permissions |

3. Create users and assign them to the appropriate group

---

## 📊 Business Logic

| Logic | Rule |
|-------|------|
| **Profit** | `selling_price − purchase_price` |
| **Revenue** | Sum of `selling_price` for all completed services |
| **Stock Deduction** | Decreases by 1 when a service request is created |
| **Low Stock Alert** | Products with `stock_quantity ≤ 2` |
| **Returned Date** | Auto-set to today when status changes to Completed |

---

## 🔒 Security

- All views protected with `@login_required`
- Role-based access enforced with `@permission_required`
- Unauthorized access returns **HTTP 403 Forbidden**
- Delete actions require POST confirmation — no accidental deletions

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Built with ❤️ using Python & Django
