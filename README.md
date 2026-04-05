# 🎬 Movie Reservation System

A fully functional backend REST API for a movie ticket reservation system — similar to BookMyShow. Built with Python, FastAPI, and MySQL.

## 🚀 Technologies Used

- **Python** — Core programming language
- **FastAPI** — Modern web framework for building APIs
- **MySQL** — Relational database
- **SQLAlchemy** — ORM for database operations
- **Pydantic** — Data validation
- **JWT (python-jose)** — Authentication using JSON Web Tokens
- **bcrypt (passlib)** — Secure password hashing
- **Uvicorn** — ASGI server

## ✅ Features

- User registration with duplicate email check
- Secure login with JWT token authentication
- Password hashing using bcrypt
- Add and list theaters
- Add and list movies
- Add seats to theaters
- Create and list movie schedules
- Book tickets with seat availability check
- View booking history by user
- Auto-generated interactive API documentation (Swagger UI)

## 📁 Project Structure
movie_reservation_system/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── user.py
│   │   ├── theater.py
│   │   ├── movie.py
│   │   ├── seat.py
│   │   ├── schedule.py
│   │   └── ticket.py
│   ├── schemas/
│   │   ├── user.py
│   │   ├── theater.py
│   │   ├── movie.py
│   │   ├── seat.py
│   │   ├── schedule.py
│   │   └── ticket.py
│   ├── routers/
│   │   ├── user.py
│   │   ├── theater.py
│   │   ├── movie.py
│   │   ├── seat.py
│   │   ├── schedule.py
│   │   └── ticket.py
│   └── services/
│       ├── user.py
│       ├── theater.py
│       ├── movie.py
│       ├── seat.py
│       ├── schedule.py
│       └── ticket.py
├── .env
└── requirements.txt

## ⚙️ How to Run

**1. Clone the repository**
git clone https://github.com/hema2106/movie-reservation-system.git
cd movie_reservation_system

**2. Install dependencies**
pip install -r requirements.txt

**3. Create `.env` file**
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=movie_reservation_db
SECRET_KEY=your_secret_key

**4. Create the database in MySQL**
CREATE DATABASE movie_reservation_db;

**5. Run the application**
uvicorn app.main:app --reload

**6. Open API documentation**
http://127.0.0.1:8000/docs

## 📌 API Endpoints

### Users
| Method | Endpoint | Description |
|---|---|---|
| POST | /users/register | Register a new user |
| POST | /users/login | Login and get JWT token |

### Theaters
| Method | Endpoint | Description |
|---|---|---|
| POST | /theaters/ | Add a new theater |
| GET | /theaters/ | Get all theaters |

### Movies
| Method | Endpoint | Description |
|---|---|---|
| POST | /movies/ | Add a new movie |
| GET | /movies/ | Get all movies |

### Seats
| Method | Endpoint | Description |
|---|---|---|
| POST | /seats/ | Add a new seat |
| GET | /seats/{theater_id} | Get all seats for a theater |

### Schedules
| Method | Endpoint | Description |
|---|---|---|
| POST | /schedules/ | Create a movie schedule |
| GET | /schedules/ | Get all schedules |

### Tickets
| Method | Endpoint | Description |
|---|---|---|
| POST | /tickets/ | Book a ticket |
| GET | /tickets/user/{user_id} | Get all tickets for a user |

## 🔐 Authentication

This project uses JWT token authentication. After login, include the token in request headers:
Authorization: Bearer your_token_here

## 📊 Database Schema

| Table | Description |
|---|---|
| users | Stores user account information |
| theater | Stores theater details |
| movie | Stores movie information |
| seat | Stores individual seats per theater |
| schedules | Links movies to theaters with date and time |
| ticket | Stores ticket bookings |

## 👩‍💻 Author

Hema — BE Computer Science Engineering, IFET College of Engineering