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
LogiTrack/
│
├── static/
│   ├── css/
│   ├── images/
│   └── js/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_parcel.html
|   ├── admin_login.html
|   ├── tracking_result.html
│   └── track.html
│
├── database.py
├── app.py
├── requirements.txt
├── models.py
├── notification.py
└── utils.py
```

## 📸 Screenshots
### Home Page

<img width="941" height="440" alt="image" src="https://github.com/user-attachments/assets/841d551c-67bf-41a5-95da-22155857aa90" />
<img width="937" height="439" alt="image" src="https://github.com/user-attachments/assets/8f10ab7a-c486-4317-9fbb-b4dbdb76d842" />


### Login Page

<img width="946" height="431" alt="image" src="https://github.com/user-attachments/assets/22acba76-71c0-47bc-99f6-489cc105eac9" />


### Register Page

<img width="931" height="437" alt="image" src="https://github.com/user-attachments/assets/2271597e-38a3-4273-88fb-276357ee592c" />

### Admin Login Page

<img width="938" height="427" alt="image" src="https://github.com/user-attachments/assets/c969646d-f4fe-488c-9726-baf2264ff132" />

### Admin Dashboard

<img width="931" height="431" alt="image" src="https://github.com/user-attachments/assets/0e704590-3936-49f4-95cd-ebd5e0e28b8b" />


### Book Parcel

<img width="931" height="433" alt="image" src="https://github.com/user-attachments/assets/b26399d9-3e62-4874-b768-89f710154ed2" />


### Track Parcel

<img width="935" height="423" alt="image" src="https://github.com/user-attachments/assets/8047a54a-3efe-4f13-9875-aa7e0c5c7f62" />
<img width="940" height="430" alt="image" src="https://github.com/user-attachments/assets/d79d4d13-d1db-4484-a8fc-5fde715f1e47" />

### MongoDB Database

#### 1. Book Parcel Database

<img width="950" height="494" alt="image" src="https://github.com/user-attachments/assets/364d9981-4464-4ab0-898c-a8170d5cdba9" />

#### 2. User Database

<img width="939" height="453" alt="image" src="https://github.com/user-attachments/assets/bd20bbcf-8759-433d-a60d-74836361c9e2" />



## 📈 Future Improvements

* Email Notifications
* SMS Notifications
* Live GPS Tracking
* QR Code Tracking
* Online Payment Integration
* Driver Management
* Delivery Analytics Dashboard


## 👩‍💻 Author

**Ankita Meshram**

---
GitHub: https://github.com/Ankita-meshram
---

## 📄 License

This project is developed for educational and learning purposes.

