📚 BookmarkHub

BookmarkHub is a full-stack Django web application that helps users organize and manage their bookmarks efficiently. It provides a secure authentication system, personal dashboard, collections, tags, search, filtering, pagination, and profile management.

---

## ✨ Features

### 🔐 Authentication

* User Registration
* User Login
* User Logout
* Change Password
* Delete Account

### 📑 Bookmark Management

* Create Bookmark
* View Bookmark Details
* Update Bookmark
* Delete Bookmark
* Public/Private Visibility
* Add Description
* Organize with Collections
* Organize with Tags

### 📂 Collections

* Create Collections
* Update Collections
* Delete Collections
* View All Collections

### 🏷️ Tags

* Create Tags
* Update Tags
* Delete Tags
* View All Tags

### 📊 Dashboard

* Total Bookmarks
* Total Collections
* Total Tags
* Recently Added Bookmarks

### 👤 User Profile

* View Profile
* Update Username
* Update Email
* Change Password
* Delete Account

### 🔍 Search & Filtering

* Search Bookmarks by Title
* Search Collections
* Search Tags
* Filter by Visibility
* Filter by Collection
* Filter by Tag
* Sort by:

  * Newest
  * Oldest
  * Alphabetical

### 📄 Pagination

* Paginated lists for:

  * Bookmarks
  * Collections
  * Tags

### 🛡️ Security

* Login Required Protection
* User Ownership Validation
* Form Validation
* CSRF Protection
* Password Validation
* Django Authentication System

### ⚙️ Django Admin

* Customized Admin Interface
* Search
* Filters
* Ordering
* List Display

---

## 🛠️ Tech Stack

* Python
* Django
* SQLite
* HTML5
* CSS3
* JavaScript
* Bootstrap

---

## 📁 Project Structure

```text
bookmarkhub/
│
├── accounts/
├── bookmarks/
├── bookmarkhub/
├── static/
├── templates/
├── manage.py
└── requirements.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/devanshvatssharma/Bookmarkhub.git
```

Navigate to the project:

```bash
cd Bookmarkhub
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser (optional):

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots
<img width="1127" height="652" alt="Screenshot 2026-07-25 203238" src="https://github.com/user-attachments/assets/8c1d04cb-3a83-477b-b7e8-3282a9fe8dd6" />
<img width="1127" height="647" alt="Screenshot 2026-07-25 203751" src="https://github.com/user-attachments/assets/ac3a8124-7c6e-4b2c-8c4d-0c8a6c711846" />
<img width="1127" height="646" alt="Screenshot 2026-07-25 203707" src="https://github.com/user-attachments/assets/325bd109-f697-447d-ac1c-00676772f745" />
<img width="1127" height="647" alt="Screenshot 2026-07-25 203959" src="https://github.com/user-attachments/assets/e830ff66-c9a1-4665-a2df-b11f5b0df1f9" />
<img width="1127" height="649" alt="Screenshot 2026-07-25 203813" src="https://github.com/user-attachments/assets/e34a27a6-5c82-422b-8e3f-03b7b2b1e816" />
<img width="1127" height="647" alt="Screenshot 2026-07-25 203843" src="https://github.com/user-attachments/assets/77fd8bf8-8c58-44ac-9624-5e2aeeea3d02" />

## 📈 Future Enhancements

* Bookmark Sharing
* Favorites
* Import/Export Bookmarks
* Browser Extension
* REST API
* Dark Mode
* Social Login
* Email Verification

---

## 👨‍💻 Author

**Devansh Sharma**

GitHub: https://github.com/devanshvatssharma

LinkedIn: *(Add your LinkedIn profile link here)*

---


