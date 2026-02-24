# 📚 Library Management System (Advanced OOP – CLI Based)

# 📌 Overview
This is a modular Library Management System built using advanced Object-Oriented Programming principles in Python.
The project demonstrates:
Encapsulation
Inheritance
Polymorphism
Modular Architecture
Custom Exception Handling
Service Layer Separation
Fine Calculation Logic
JSON-based Storage (Extendable)
Clean CLI Interface
This project is designed to simulate a real-world backend system before converting it into a REST API.

# 🏗 Project Architecture
library_management/
│
├── models/
│   ├── person.py
│   ├── user.py
│   ├── admin.py
│   ├── book.py
│   ├── transaction.py
│
├── services/
│   ├── library_service.py
│   ├── fine_service.py
│
├── utils/
│   ├── validators.py
│   ├── exceptions.py
│   ├── id_generator.py
│
├── data/
│   ├── storage_manager.py
│
├── main.py

# 🧠 Design Principles Applied
# 🔐 Encapsulation
All attributes are private (__variable)
Access controlled through getters/setters
# 🧬 Inheritance
User and Admin inherit from Person
# 🔄 Polymorphism
display_info() overridden in multiple classes
# 🏛 Layered Architecture
Models → Data structures
Services → Business logic
Utils → Validation & exceptions
CLI → User interaction layer

# 🚀 Features
# 📚 Book Management
Add book
View books
Track availability
Search functionality (extendable)
# 👤 User Management
Register user
Track issued books
# 🔁 Issue & Return System
Issue book to user
Return book
Automatic fine calculation
# 💰 Fine System
7-day borrowing limit
₹5 per day late fine
Automated fine calculation via FineService
# ⚠ Error Handling
Custom exceptions:
BookNotAvailableError
BookNotFoundError
UserNotFoundError

# 🖥 How to Run
# 1️⃣ Clone the repository
Bash
Copy code
git clone https://github.com/your-username/library-management-system.git
cd library-management-system

# 2️⃣ Run the application
Bash
Copy code
python main.py

# 📋 CLI Menu
1. Add Book
2. Register User
3. View Books
4. Issue Book
5. Return Book
6. Exit
   
# 📊 System Flow
CLI
 ↓
LibraryService
 ↓
Models (Book/User/Transaction)
 ↓
FineService
 ↓
Exceptions & Validators

# 🛠 Technologies Used
Python 3
OOP Principles
JSON Storage
Modular Design Pattern

# 🧪 Future Improvements
Add persistent JSON saving for full system state
Convert to REST API using Flask
Add SQLite / MySQL integration
Implement JWT authentication
Add Unit Testing (pytest)
Dockerize application
Deploy on cloud (Render / Railway)

# 🎯 Learning Outcomes
This project demonstrates strong understanding of:
Object-Oriented Programming
Separation of Concerns
Backend Architecture Thinking
Clean Code Structure
Exception Handling
Real-world business logic implementation

# 👩‍💻 Author
Sangita Bera
Backend Developer | Python Enthusiast | Learning AI/ML

# ⭐ If You Like This Project
Give it a star ⭐ and feel free to fork and improve it.
