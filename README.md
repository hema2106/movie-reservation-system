# 🎬 Movie Reservation System

A fully functional **backend REST API** for booking movie tickets, built with **FastAPI** and **MySQL**. Supports user authentication, movie scheduling, seat management, and ticket booking.

---

## 🚀 Features

- 🔐 **JWT Authentication** — Secure register & login system
- 🎥 **Movie Management** — Add and list movies
- 🏟️ **Theater & Seat Management** — Manage theaters and available seats
- 📅 **Schedule Management** — Create and view movie schedules
- 🎟️ **Ticket Booking** — Book tickets with payment status tracking
- 📖 **Auto API Docs** — Interactive Swagger UI at `/docs`

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Core language |
| FastAPI | Web framework |
| MySQL | Database |
| SQLAlchemy | ORM |
| Alembic | Database migrations |
| JWT (jose) | Authentication |
| Uvicorn | ASGI server |
| Swagger UI | API documentation |

---

## 📁 Project Structure

```
movie_reservation_system/
│
├── app/
│   ├── main.py              # App entry point
│   ├── database.py          # DB connection setup
│   ├── deps.py              # Dependency injection
│   ├── models/              # SQLAlchemy models
│   │   ├── ticket.py
│   │   └── enums.py
│   ├── routers/             # API route handlers
│   │   ├── user.py
│   │   ├── movie.py
│   │   ├── theater.py
│   │   ├── seat.py
│   │   ├── schedule.py
│   │   └── ticket.py
│   ├── schemas/             # Pydantic schemas
│   │   └── ticket.py
│   └── services/            # Business logic
│       ├── user.py
│       └── ticket.py
│
├── alembic/                 # DB migration files
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/hema2106/movie-reservation-system.git
cd movie-reservation-system
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory:
```env
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/movie_db
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Run database migrations
```bash
alembic upgrade head
```

### 6. Start the server
```bash
uvicorn app.main:app --reload
```

### 7. Open API docs
```
http://127.0.0.1:8000/docs
```

---

## 🔑 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login and get JWT token |

### Movies
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/movies/` | Add a movie |
| GET | `/movies/` | List all movies |

### Theaters & Seats
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/theaters/` | Add a theater |
| POST | `/seats/` | Add seats to theater |
| GET | `/seats/` | List all seats |

### Schedules
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/schedules/` | Create a schedule |
| GET | `/schedules/` | List all schedules |

### Tickets
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tickets/` | Book a ticket 🎟️ |
| GET | `/tickets/` | View my bookings |
| GET | `/tickets/{id}` | Get ticket by ID |
| DELETE | `/tickets/{id}` | Cancel a ticket |

---

## 🔐 Authentication Guide

1. Register at `POST /auth/register`
2. Login at `POST /auth/login` — copy the `access_token`
3. Click **Authorize** in Swagger UI
4. Enter: `Bearer <your_token>`
5. All protected endpoints are now accessible ✅

---

## 📸 Sample Response — Book Ticket

**POST** `/tickets/`

```json
{
  "ticket_id": 2,
  "user_id": 5,
  "schedule_id": 2,
  "seat_id": 1,
  "booking_time": "2026-04-21T10:11:15",
  "payment_status": "pending"
}
```

---

## 👩‍💻 Author

**Hema Venkatesan**  
B.E. Computer Science Engineering — IFET College of Engineering  
🔗 [LinkedIn](https://linkedin.com/in/hema-v-988a66337) | 🐙 [GitHub](https://github.com/hema2106)