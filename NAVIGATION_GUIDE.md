# TARMS Navigation Guide

## Login & Signup Pages

### Student Flow

#### Student Login
- **URL**: `http://localhost:3000/`
- **Credentials**: 
  - Username: `student`
  - Password: `student`
- **Links on page**:
  - "Forgot Password?" → `/forgotPassword`
  - "Sign-up here" → `/signUp` (Student Signup)
  - "Log-in here" (Faculty) → `/facultylogin`

#### Student Signup
- **URL**: `http://localhost:3000/signUp`
- **Form Fields**:
  - Name
  - User ID
  - Email
  - Date of Birth
  - Mobile Number
  - Password
- **Links on page**:
  - "Log-in here" → `/` (Student Login)
  - "Sign-up here" (Faculty) → `/faculty_sign`

---

### Faculty Flow

#### Faculty Login
- **URL**: `http://localhost:3000/facultylogin`
- **Credentials**: 
  - Username: `admin`
  - Password: `admin`
- **Links on page**:
  - "Sign-up here" → `/faculty_sign` (Faculty Signup) ✅ **NEWLY ADDED**
  - "Log-in here" (Student) → `/` ✅ **NEWLY ADDED**

#### Faculty Signup
- **URL**: `http://localhost:3000/faculty_sign`
- **Form Fields**:
  - Name
  - User ID
  - Email (thapar.edu)
  - Position
  - Mobile Number
  - Password
- **Links on page**:
  - "Log-in here" → `/facultylogin` (Faculty Login)

---

## Complete Navigation Map

```
┌─────────────────────────────────────────────────────────────┐
│                    TARMS Navigation                          │
└─────────────────────────────────────────────────────────────┘

STUDENT SIDE:
┌──────────────────┐
│  Student Login   │  http://localhost:3000/
│  (/)             │  
└────────┬─────────┘
         │
         ├──→ "Sign-up here" ──→ ┌──────────────────┐
         │                        │  Student Signup  │
         │                        │  (/signUp)       │
         │                        └──────────────────┘
         │
         ├──→ "Forgot Password?" ──→ ┌──────────────────┐
         │                            │ Forgot Password  │
         │                            │ (/forgotPassword)│
         │                            └──────────────────┘
         │
         └──→ "Faculty Login" ──→ (See Faculty Side)


FACULTY SIDE:
┌──────────────────┐
│  Faculty Login   │  http://localhost:3000/facultylogin
│  (/facultylogin) │  
└────────┬─────────┘
         │
         ├──→ "Sign-up here" ──→ ┌──────────────────┐
         │                        │  Faculty Signup  │
         │                        │  (/faculty_sign) │
         │                        └──────────────────┘
         │
         └──→ "Student Login" ──→ (See Student Side)
```

---

## Quick Access URLs

| Page | URL | Purpose |
|------|-----|---------|
| **Student Login** | `http://localhost:3000/` | Main login page |
| **Student Signup** | `http://localhost:3000/signUp` | Register new student |
| **Faculty Login** | `http://localhost:3000/facultylogin` | Faculty login page |
| **Faculty Signup** | `http://localhost:3000/faculty_sign` | Register new faculty |
| **Forgot Password** | `http://localhost:3000/forgotPassword` | Password recovery |

---

## What Was Fixed

### Issue: Faculty Signup Link Missing

**Problem**: The faculty login page didn't have a link to the faculty signup page.

**Solution**: Added two links to `/views/facultylogin.hbs`:
1. ✅ "New Faculty? Sign-up here" → `/faculty_sign`
2. ✅ "Are you a Student? Log-in here" → `/`

**Updated File**: `/Users/adityasinha/Downloads/TARMS-main/views/facultylogin.hbs`

---

## How to Access Faculty Signup

### Method 1: Direct URL
Navigate to: `http://localhost:3000/faculty_sign`

### Method 2: From Faculty Login Page
1. Go to `http://localhost:3000/facultylogin`
2. Click "Sign-up here" under "New Faculty?"

### Method 3: From Student Signup Page
1. Go to `http://localhost:3000/signUp`
2. Click "Sign-up here" under "Are you a Faculty?"

---

## Testing the Navigation

### Test Faculty Signup Flow:
1. Start server: `node src/index.js`
2. Open browser: `http://localhost:3000/facultylogin`
3. Click "Sign-up here" (should go to `/faculty_sign`)
4. Fill in the form:
   - Name: Test Faculty
   - User ID: testfaculty
   - Email: test@thapar.edu
   - Position: Professor
   - Mobile: 1234567890
   - Password: Test@123
5. Click "Sign-Up"
6. Should redirect to login page

### Verify New Faculty Login:
1. Go to `http://localhost:3000/facultylogin`
2. Login with:
   - Username: `testfaculty`
   - Password: `Test@123`
3. Should redirect to faculty dashboard

---

## Summary

✅ **Faculty signup option is now visible** on the faculty login page  
✅ **Easy navigation** between student and faculty login/signup pages  
✅ **All routes working** correctly  
✅ **Consistent UI** across all login/signup pages  

The faculty signup link was missing from the faculty login page, but it has now been added!
