# TARMS Login Troubleshooting Guide

## Default Login Credentials

### Student Login (Main Page: http://localhost:3000)
```
Username: student
Password: student
```

### Faculty Login (Faculty Page: http://localhost:3000/facultylogin)
```
Username: admin
Password: admin
```

## Common Issues & Solutions

### Issue 1: Login page keeps reloading
**Cause**: Wrong credentials or database not seeded
**Solution**:
1. Make sure MongoDB is running: `pgrep -l mongod`
2. Seed the database: `node seed_users.js`
3. Use correct credentials above

### Issue 2: "Wrong credentials" message
**Cause**: Username or password doesn't match database
**Solution**: Use the exact credentials listed above (case-sensitive)

### Issue 3: Server not starting
**Cause**: MongoDB not running or port 3000 in use
**Solution**:
1. Start MongoDB: `brew services start mongodb-community`
2. Check if port is free: `lsof -i :3000`

## How to Start the Application

1. **Start MongoDB** (if not running):
   ```bash
   brew services start mongodb-community
   ```

2. **Seed the database** (first time only):
   ```bash
   node seed_users.js
   node seed_rooms.js
   ```

3. **Start the server**:
   ```bash
   node src/index.js
   ```

4. **Open browser**:
   Navigate to `http://localhost:3000`

5. **Login**:
   - Use student credentials: `student` / `student`
   - Or faculty login: `admin` / `admin` (at `/facultylogin`)

## Expected Behavior

### Successful Student Login:
- Redirects to: `http://localhost:3000/home?uid=<user_id>`
- Shows: "Welcome Aditya Sinha"
- Displays: Available rooms for booking

### Successful Faculty Login:
- Redirects to: `http://localhost:3000/faculty?uid=<user_id>`
- Shows: "Welcome Dr. Ashima Singh"
- Displays: Pending room requests

## Creating New Users

### Register New Student:
1. Click "Sign-up here" on login page
2. Fill in the form
3. Login with new credentials

### Register New Faculty:
1. Go to `/faculty_sign`
2. Fill in the form
3. Login at `/facultylogin`

## Checking Database

To verify users exist in database:
```bash
mongosh
use test
db.users.find()
db.faculties.find()
```

## Server Logs to Watch

When you start the server, you should see:
```
Database connected successfully
Server running on http://localhost:3000
```

When you login successfully, you should see:
```
(No error messages)
```

If login fails, you'll see:
```
Wrong credentials
```
or
```
Some error occured
```
