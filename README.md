# 📦 LogiTrack - Parcel Management System

LogiTrack is a **Django-based Parcel Management System** that helps users book, manage, and track parcels easily. The system provides a simple interface for parcel registration and stores parcel details securely using MongoDB.

---

## 🚀 Features

* 👤 User Registration & Login
* 📦 Parcel Booking System
* 📝 Store Sender and Receiver Details
* 🔍 Parcel Tracking Management
* 📊 Manage Parcel Records
* ☁️ MongoDB Atlas Database Integration
* 🌐 Django Web Application

---

## 🛠️ Technologies Used

### Backend

* Python
* Django Framework

### Frontend

* HTML5
* CSS3
* Bootstrap

### Database

* MongoDB Atlas

### Tools

* VS Code
* Git & GitHub

---

## 📂 Project Structure

```
LogiTrack/
│
├── manage.py
│
├── LogiTrack/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── parcel/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── templates/
│
├── static/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/Ankita-meshram/LogiTrack.git
```

### 2. Open Project Folder

```bash
cd LogiTrack
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows**

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure MongoDB

Create MongoDB Atlas connection and add your MongoDB URI in Django settings/environment variables.

Example:

```
mongodb+srv://username:password@cluster.mongodb.net/
```

---

### 6. Run Database Migration

```bash
python manage.py migrate
```

---

### 7. Django admin login

```bash
python manage.py createsuperuser
```
change password admin:

```
python manage.py changepassword admin
```

---

### 8. Start Django Server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 📸 Application Screenshots
Example:

* Home Page
  
  <img width="936" height="439" alt="image" src="https://github.com/user-attachments/assets/0b0642f8-b8cd-4616-9b98-23e00abf90bb" />

* Login Page
  
   <img width="517" height="304" alt="image" src="https://github.com/user-attachments/assets/88e22d88-0853-4d7c-9c44-3bb200fd7e35" />

* signup Page
  
  <img width="583" height="409" alt="image" src="https://github.com/user-attachments/assets/dd4aa1cc-2342-4877-9ca0-deea86e19735" />

* Parcel Booking Page
  
  <img width="796" height="442" alt="image" src="https://github.com/user-attachments/assets/2eabd163-ea34-4b0c-aee7-780f05256105" />
  
  <img width="523" height="326" alt="image" src="https://github.com/user-attachments/assets/4604396b-b01a-4f84-a15e-a849f15eb01a" />

* Parcel Tracking Page
  
   <img width="449" height="281" alt="image" src="https://github.com/user-attachments/assets/060a12d3-6788-462a-bcdc-6a375647a768" />
  
   <img width="403" height="274" alt="image" src="https://github.com/user-attachments/assets/d4470d27-8fe9-4e05-b683-18abed97e5ac" />

* Admin Login page
  
  <img width="356" height="198" alt="image" src="https://github.com/user-attachments/assets/11cd8638-1875-46ea-82a8-eab968bdd246" />

* Dashboard
  
  <img width="827" height="438" alt="image" src="https://github.com/user-attachments/assets/65a0c4fb-44a8-4959-90ae-fe0e367d5872" />


---

## 🔮 Future Enhancements

* Real-time parcel tracking
* Email/SMS notifications
* Delivery partner management
* Payment integration
* Admin analytics dashboard

---

## 👩‍💻 Developer

**Ankita Meshram**

MCA Student 

---

## 📄 License

This project is developed for educational purposes.
