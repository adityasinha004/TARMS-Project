# TARMS - Auditorium and Room Management System

A web-based room booking and management system for educational institutions.

## Quick Start

### Prerequisites
- Node.js installed
- MongoDB installed and running

### Setup & Run

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start MongoDB:**
   ```bash
   brew services start mongodb-community
   ```

3. **Seed the database:**
   ```bash
   node seed_users.js
   node seed_rooms.js
   ```

4. **Start the server:**
   ```bash
   node src/index.js
   ```

5. **Open browser:**
   Navigate to `http://localhost:3000`

## Default Login Credentials

### Student Login
```
Username: student
Password: student
```

### Faculty Login (at /facultylogin)
```
Username: admin
Password: admin
```

## Features

- Student room booking system
- Faculty approval workflow
- Real-time room availability
- AI-based usage prediction
- User authentication and session management
- Booking history and management

## Tech Stack

- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Frontend**: Handlebars (HBS), HTML, CSS, JavaScript
- **Prediction**: Python (Matplotlib)

## Project Structure

```
TARMS-main/
├── src/
│   ├── controller/     # Business logic
│   ├── models/         # MongoDB schemas
│   ├── routes/         # API routes
│   ├── predict_usage.py # Prediction script
│   └── index.js        # Server entry point
├── views/              # HBS templates
├── public/             # Static files (CSS, JS, images)
├── seed_users.js       # Database seeding
└── seed_rooms.js       # Room data seeding
```

## License

This project is for educational purposes.
