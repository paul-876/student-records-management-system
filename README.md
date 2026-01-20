## Student Registration System

### 1. Project Title
**Student Registration System**

### 2. Project Description
This is a **simple student registration system** that allows an administrator to add, view, edit, and delete student records.  
The system is designed as a basic CRUD (Create, Read, Update, Delete) web application using HTML, CSS, Python (Flask), and MySQL.  
It is suitable for small institutions or as a learning project for beginners in web development.

### 3. Problem Statement
Many small institutions still keep student records on paper or in simple notebooks.  
This causes several challenges:
- **Difficult to find information quickly** – staff must flip through pages to locate a single student.
- **Poor data safety** – paper records can be lost, damaged, or misplaced.
- **Hard to update records** – editing details on paper can become messy and confusing.

A **simple computerized system** can solve these problems by storing records in a structured database, allowing quick search, easy updates, and safer storage.

### 4. Technologies Used
- **Interface**: HTML + basic CSS  
- **Logic / Backend**: Python (Flask framework)  
- **Database / Storage**: MySQL  
- **Editor**: Visual Studio Code (VS Code)  
- **Server / Runtime**: Python Flask development server +  local MySQL server

### 5. Features
- **Add Student Details**  
  - Input student name, registration number, and course.
- **View Student List**  
  - Display all saved student records in a table.
- **Edit Student Records**  
  - Update name, registration number, and course for an existing student.
- **Delete Student Records**  
  - Remove a student record permanently from the database.
- **Simple, Clean Interface**  
  - Easy-to-use form and table-based layout for beginners and non-technical users.

### 6. How to Install and Run the System

#### 6.1. Prerequisites
- **Python 3.7 or higher** installed on your computer.  
- **MySQL** .  
- **Web browser** (Chrome, Firefox, Edge, etc.).  
- **pip** (Python package installer, usually comes with Python).

#### 6.2. Step 1: Install Python Dependencies
1. Open a terminal or command prompt in the project folder (`student portal`).  
2. Install the required Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```
   This will install Flask and mysql-connector-python.

#### 6.3. Step 2: Create the Database
1. Start **MySQL**.
2. On MYSQL terminal paste the following commands:
Create database Student_db;
use Student_db;
3. With `student_db` selected.
4. Copy and paste the SQL script from `database.sql` (included in this project) and click **Enter** to create the `students` table.

#### 6.4. Step 3: Configure Database Connection (if needed)
1. Open `config.py` in a text editor (VS Code).  
2. Check the following settings and adjust if necessary:
   - `'host': 'localhost'`
   - `'user': 'root'` (default MYSQL user)
   - `'password': 'Escape254'` (current project setting; change if your MySQL password differs)
   - `'database': 'student_db'` (or your chosen database name)

#### 6.5. Step 4: Run the Application
1. Make sure **MySQL** is running.
2. Open a terminal or command prompt in the project folder (`student portal`).
3. Run the Flask application:
   ```bash
   python app.py
   ```
   You should see output like:
   ```
   * Running on http://127.0.0.1:5500
   ```
4. Open your browser and go to:  
   - `http://127.0.0.1:5500` or `http://localhost:5500`
5. You should see:
   - A **student registration form** at the top.
   - A **table of registered students** below the form.

You can now:
- Add new students using the form.
- View all students in the table.
- Edit or delete existing records using the action buttons/links.

### 7. Login Credentials for Testing
This project is designed for **one administrator user only** and **does not include a login system**.  
No username or password is required to access the system.


---

### Project Overview (Summary)
This project is a **basic computer system** that allows an administrator to register students and view their details.  
It is intentionally **simple** so that beginners can understand the full flow from **data entry form**, to **database storage**, to **displaying and managing records** on a web page.

### Problem Statement (Summary)
Small institutions using paper-based records face problems with speed, safety, and ease of updating records.  
This simple computerized system provides:
- Faster access to student data
- Safer storage of records in a database
- Easier updating and deletion of student details

### Project Objectives
- **Main Objective**  
  - To create a simple student registration system using basic programming skills.

- **Specific Objectives**
  - **Design a simple data entry form** for student details.  
  - **Save student details** in a MySQL database.  
  - **Display a list of registered students** in a table.  
  - **Allow editing and deleting** of student records.  
  - **Present the project using GitHub** as a hosting and version control platform.

### Scope of the System
- **Included**
  - One user (administrator, no login).
  - Add student details.
  - View list of students.
  - Edit and delete student records.

- **Excluded**
  - Login system / authentication.
  - Multiple user roles.
  - Reports and analytics.
  - Online (internet-based) features.

### System User
- **Administrator only**  
  - Performs all operations: add, view, edit, and delete students.

### Functional Requirements
1. **Input student details**: name, registration number, and course.  
2. **Save data** to the MySQL database.  
3. **Display saved records** in a list/table format.  
4. **Update and delete records** using simple actions on the list.

### Non-Functional Requirements
1. **Easy to use** – simple layout and clear labels.  
2. **Simple interface** – basic colors, minimal styling, and no complex navigation.

### Database Design
- **Database Name**: `student_db` (can be changed in `config.py`)  
- **Table Name**: `students`

**Students Table Structure**
- `student_id` (INT, primary key, auto-increment)  
- `name` (VARCHAR)  
- `registration_number` (VARCHAR)  
- `course` (VARCHAR)

The SQL script to create this table is provided in `database.sql`.

### Project Deliverables (Checklist)
This project repository helps you prepare the following deliverables:

- **Source code**  
  - All Python, HTML, CSS files in this repository (app.py, config.py, templates/index.html).
- **Database file or SQL script**  
  - Included as `database.sql`.
- **Short user guide**  
  - You can adapt the “How to Install and Run the System” section from this README.
- **GitHub link**  
  - Upload this project to your GitHub account and share the repository link as part of your submission.

### Repository Contents (cleaned)
- `app.py` — Flask application (CRUD logic + routes)
- `config.py` — database connection settings (MySQL)
- `templates/index.html` — UI template with form and table
- `requirements.txt` — Python dependencies (Flask, mysql-connector-python)
- `database.sql` — SQL to create `students` table
- `README.md` — this guide

---

### How to Use This Project
1. **Download or clone** this repository.  
2. **Install dependencies** using `pip install -r requirements.txt`.  
3. **Configure** the database using `database.sql` and update `config.py` if needed.  
4. **Test** all features (add, view, edit, delete).  


