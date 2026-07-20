# 🚚 LogiTrack

**LogiTrack** is a Parcel Tracking & Delivery Status Notification System developed using **Python, Django, and MongoDB**. The system allows users to book parcels, track deliveries using a unique tracking ID, and receive delivery status updates. Administrators can manage parcels and update delivery statuses through an admin dashboard.

---

## 📌 Project Information

* **Project Name:** LogiTrack
* **Subtitle:** Parcel Tracking & Delivery Status Notification System
* **Domain:** Logistics

---

## ✨ Features

* Parcel Booking
* Unique Tracking ID Generation
* Parcel Status Tracking
* Delivery Status Notifications
* Admin Dashboard
* Parcel Search by Tracking ID
* MongoDB Database Integration
* REST API using Django REST Framework

---

## 🛠 Technologies Used

* Python 3
* Django
* Django REST Framework (DRF)
* MongoDB
* HTML
* CSS
* JavaScript
* Bootstrap
* Git
* GitHub

---

## 📚 Concepts Implemented

### 1 – Fundamentals

* Lists for delivery status stages
* Dictionary for parcel information
* Conditional statements for delivery progress

### 2 – Functions & Modules

* `uuid` module for generating Tracking IDs
* `datetime` module for status updates
* Exception handling for invalid pincodes

### 3 – OOP, Regex & Threading

* `Parcel` class
* `StatusTracker` class
* `NotificationEngine` class
* Regular Expressions for validating phone numbers and pincodes
* Threading for sending delivery notifications

### 4 – MongoDB

* Parcel Collection
* Status History Collection
* CRUD Operations
* Search Parcel using Tracking ID

### 5 – Django

* Parcel Booking Form
* Public Tracking Page
* Admin Dashboard
* Django REST Framework APIs

---

## 💻 Software Required

* Python 3.12 or later
* MongoDB Community Server
* Visual Studio Code
* Git
* Postman

---

## 📥 Clone Repository

```bash
git clone https://github.com/Ankita-meshram/LogiTrack.git
```

```bash
cd LogiTrack
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 How to Run the Project
Step 1: Install Python :

Download and install Python 3.x from the official website.

After installation, verify it:
```
python --version
```

Step 2: Clone the Repository :
```
git clone https://github.com/Ankita-meshram/LogiTrack.git
cd Logitrack_python
```

Step 3: Create a Virtual Environment :
```
python -m venv venv
```

Activate it on Windows:
```
venv\Scripts\activate
```

Step 4: Install Required Packages :
```
pip install flask
pip install pymongo
pip install flask-login
pip install python-dotenv
```
Save all installed packages:
```
pip freeze > requirements.txt
```

Step 5: Run the Application :
```
python app.py
```
Open your browser and visit:
```
http://127.0.0.1:5000
```
---

## 📂 Project Structure

```text
LogiTrack_python/
│
├── static/
│ ├── css/
│ │ └── style.css
│ │
│ ├── images/
│ │ ├── truck.gif
│ │ └── truck.png
│ │
│ └── js/
│
├── templates/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── add_parcel.html
│ └── tracking_result.html
│
├── mongodb/
│
├── app.py
├── database.py
├── models.py
├── notification.py
├── utils.py
│
├── requirements.txt
├── requirements.py
└── venv/
```

---

## 📡 APIs

* POST /book-parcel/
* GET /track/<tracking_id>/
* GET /api/parcels/
* PUT /api/update-status/
* DELETE /api/delete-parcel/

---

## 📈 Future Improvements

* Email Notifications
* SMS Notifications
* Live GPS Tracking
* QR Code Tracking
* Online Payment Integration
* Driver Management
* Delivery Analytics Dashboard

---

## 👩‍💻 Author

**Ankita Meshram**

GitHub: https://github.com/Ankita-meshram

---

## 📄 License

This project is developed for educational and learning purposes.

