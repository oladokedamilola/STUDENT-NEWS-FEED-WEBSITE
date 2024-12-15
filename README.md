# Student News Feed Website

A web application that serves as a dedicated platform for university students to stay informed, interact, and share posts. It incorporates student identity verification, user roles, and an approval-based content creation system.

## Features

1. **Student Identity Verification**
   - Students are required to enter their **matriculation number**.
   - The matriculation number is checked against the university's database to verify identity.

2. **Account Creation**
   - Once verified, students can create an account.

3. **User Roles**
   - **Read-Only Users**: By default, all students have read-only access. They can:
     - View posts
     - Like posts
     - Comment on posts
   - **Content Creators**: Students can apply to become content creators via an "Apply to be a Creator" form in the navbar. If approved by the admin, they gain:
     - Access to the "Create Post" functionality in the navbar
     - Notifications for interactions (likes/comments) on their posts

4. **Admin Review**
   - Admins receive and review "Apply to be a Creator" forms in the backend.
   - Admin approval grants students the ability to create posts.

5. **Notifications**
   - Creators receive notifications for interactions on their posts.

---

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **Database**: SQLite (for development) and MySQL/PostgreSQL (for production)
- **Authentication**: Custom student matriculation number verification

---

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites
- Python 3.x
- Git

### Clone the Repository
```bash
git clone https://github.com/oladokedamilola/STUDENT-NEWS-FEED-WEBSITE.git
cd STUDENT-NEWS-FEED-WEBSITE
```

### Set Up the Environment
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up the database:
   ```bash
   python manage.py migrate
   ```
3. Run the server:
   ```bash
   python manage.py runserver
   ```

4. Visit the application at:
   ```
   http://127.0.0.1:8000/
   ```

---

## Screenshots

Here are some screenshots of the Student News Feed Website:

### 1. **Homepage**
![Homepage](screenshots/homepage.png)

### 2. **Matriculation Number Verification**
![Verification](screenshots/verification.png)

### 3. **Apply to be a Creator Form**
![Creator Form](screenshots/apply_creator.png)

### 4. **Create Post (For Approved Creators)**
![Create Post](screenshots/create_post.png)

### 5. **Notifications for Post Interactions**
![Notifications](screenshots/notifications.png)


---

## How It Works

1. **User Verification**: 
   - Students provide their matriculation number for identity verification.

2. **Account Creation**:
   - Verified students can create accounts.

3. **Read-Only Access**:
   - Students can read posts, like, and comment.

4. **Creator Role**:
   - Students apply via a form in the navbar.
   - Admins approve or reject applications in the backend.
   - Approved creators can:
     - Create posts
     - Receive notifications for interactions on their posts.

---

## Contributing
Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a Pull Request.

