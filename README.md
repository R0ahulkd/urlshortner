<h1 align="center">🔗 Django URL Shortener</h1>

<p align="center">
  🚀 A powerful and minimal Django-based web application for creating custom short URLs. <br/>
  🔐 Built with authentication, form validation, and responsive design.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Django-5.2-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" />
</p>

---

## 🌟 Features

- 🔒 User registration & login system
- 🔗 Shorten long URLs with unique codes
- 📊 Track URL redirection stats
- 📎 Copy-to-clipboard support
- 📱 Fully responsive UI (Bootstrap)
- 💥 Error messages with validations
- 🎨 Floating label form design

---

## 🛠️ Tech Stack

| Layer      | Technology                      |
|------------|----------------------------------|
| 👨‍💻 Backend   | Python, Django, SQLite/MySQL       |
| 🎨 Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| 🗃️ Forms     | Django Forms, UserCreationForm     |

---

## 📸 Screenshots

![{5D317C37-057F-49A5-83FA-611D68935F7C}](https://github.com/user-attachments/assets/4b3f2443-4a3a-42f5-bc1a-fcd0bbf2571f)
![{4CF9771F-DD39-4398-8156-EEE5CB079AE3}](https://github.com/user-attachments/assets/0e740763-7772-4847-8391-384cdc4b576f)
![{99D4DDAA-EDBA-43E9-9F28-1BE275394B2C}](https://github.com/user-attachments/assets/7f024781-6cda-4336-93df-4e4dde9e2560)
![{1C872670-7B66-4DEC-B280-AF1D7B6A0ACC}](https://github.com/user-attachments/assets/5e6c58d8-bb7d-47ee-8b47-3df042c5f414)





---

## 🚀 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/R0ahulkd/django-urlshortener.git
cd django-urlshortener

# 2. Create virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate      # On Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (optional)
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
