# TARMS - Thapar Auditorium and Room Management System

## Project Overview

**TARMS (Thapar Auditorium and Room Management System)** is a comprehensive web-based application designed to streamline the booking, approval, and management of auditoriums and rooms at Thapar Institute of Engineering & Technology. The system eliminates manual booking processes, reduces waiting times, and improves the accuracy of room allocation and scheduling.

## 🎯 Project Objectives

- **Automate Room Booking Process**: Replace manual booking systems with a digital platform
- **Streamline Approval Workflow**: Enable faculty to efficiently approve/reject booking requests
- **Improve Resource Utilization**: Optimize room allocation and reduce conflicts
- **Enhance User Experience**: Provide intuitive interfaces for students and faculty
- **Maintain Audit Trail**: Keep comprehensive records of all booking activities

## 🏗️ System Architecture

### Technology Stack
- **Backend**: Node.js with Express.js framework
- **Database**: MongoDB with Mongoose ODM
- **Frontend**: Handlebars (HBS) templating engine
- **Session Management**: Express-session with MongoDB store
- **Authentication**: Custom session-based authentication
- **Development**: Nodemon for auto-restart during development

### Core Components

#### 1. **Server Configuration** (`src/index.js`)
- Express server setup with middleware configuration
- MongoDB connection management
- Session configuration with MongoDB store
- Static file serving and view engine setup
- Port 3000 for development server

#### 2. **Routing System** (`src/routes/main.js`)
- Comprehensive route handling for all user interactions
- Authentication middleware for protected routes
- Separate routes for students and faculty
- API endpoints for form submissions and data operations

#### 3. **Data Models** (`src/models/`)
- **User Model**: Student information and authentication
- **Faculty Model**: Faculty member details and credentials
- **Rooms Model**: Room/auditorium information and status
- **Booking Form Model**: Detailed booking request information
- **Contact Model**: Contact form submissions
- **Feedback Model**: User feedback collection
- **Reset Password Model**: Password reset functionality

## 👥 User Roles and Features

### 🎓 Student Features
- **User Registration**: Sign up with personal details
- **Login/Logout**: Secure authentication system
- **Room Booking**: Submit booking requests for events
- **Request Management**: View and track booking status
- **Profile Management**: Update personal information
- **Password Management**: Change password functionality
- **Contact & Feedback**: Submit inquiries and feedback

### 👨‍🏫 Faculty Features
- **Faculty Registration**: Separate signup process for faculty
- **Booking Approval**: Review and approve/reject student requests
- **Room Management**: View room details and booking information
- **Profile Management**: Update faculty information
- **Password Management**: Secure password change functionality
- **Dashboard**: Overview of pending requests

## 📊 Database Schema

### User Schema
```javascript
{
    Name: String,
    UserID: String (unique),
    eMail: String (unique),
    Member_type: String,
    MobileNumber: Number,
    DOB: Date,
    Password: String
}
```

### Faculty Schema
```javascript
{
    fac_name: String,
    position: String,
    uname: String (unique),
    mob: Number,
    Member_type: String,
    eMail: String (unique),
    password: String (unique)
}
```

### Rooms Schema
```javascript
{
    Room_Number: String,
    Room_Name: String,
    Status: String
}
```

### Booking Form Schema
```javascript
{
    Room_Name: String,
    userid: String,
    Name: String,
    branch: String,
    year: Number,
    MobileNumber: Number,
    society: String,
    eventNames: String,
    purpose: String,
    eventDate: Date,
    eventTime: String,
    eventTime1: String,
    people: Number,
    AC: String,
    SS: String,
    Status: String,
    timestamps: true
}
```

## 🔐 Security Features

- **Session-based Authentication**: Secure user sessions with MongoDB storage
- **Password Protection**: Encrypted password storage
- **Route Protection**: Authentication middleware for protected routes
- **Session Management**: Automatic session expiration (15 minutes)
- **Unique Constraints**: Email and username uniqueness validation

## 🚀 Key Functionalities

### 1. **Booking Workflow**
1. Student logs in and views available rooms
2. Student fills out detailed booking form
3. Request is submitted with "Requested" status
4. Faculty reviews the request
5. Faculty approves/rejects the request
6. Status updates to "Approved" or "Rejected"

### 2. **Room Management**
- Real-time room status tracking
- Availability checking before booking
- Conflict prevention system
- Room details and specifications

### 3. **User Management**
- Separate registration for students and faculty
- Profile management and updates
- Password reset functionality
- Contact and feedback systems

## 📱 User Interface

### Student Interface
- **Home Dashboard**: Available rooms overview
- **Booking Form**: Detailed event information submission
- **My Requests**: Track booking status and history
- **Profile Management**: Personal information updates
- **Contact/Feedback**: Communication channels

### Faculty Interface
- **Faculty Dashboard**: Pending requests overview
- **Room Details**: Detailed booking information
- **Approval System**: Accept/reject booking requests
- **Profile Management**: Faculty information updates

## 🛠️ Installation and Setup

### Prerequisites
- Node.js (v14 or higher)
- MongoDB (local installation required)
- npm package manager

### Installation Steps
1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd TARMS-main
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start MongoDB service**
   ```bash
   mongod
   ```

4. **Run the application**
   ```bash
   npm run server
   ```

5. **Access the application**
   - Open browser and navigate to `http://localhost:3000`

## 📋 API Endpoints

### Authentication
- `POST /api/login` - Student login
- `POST /api/loginfaculty` - Faculty login
- `POST /api/signIn` - Student registration
- `POST /api/faculty_sign` - Faculty registration

### Booking Management
- `POST /api/book_form` - Submit booking request
- `POST /api/response` - Faculty response to booking
- `POST /api/deleteRequest` - Delete booking request

### User Management
- `POST /api/changePassword` - Change student password
- `POST /api/FacultyChangePassword` - Change faculty password
- `POST /api/changeInfo` - Update student information
- `POST /api/FacultyChangeInfo` - Update faculty information

### Communication
- `POST /api/contact` - Submit contact form
- `POST /api/feedback` - Submit feedback
- `POST /api/reset` - Password reset

## 🎨 Frontend Features

### Responsive Design
- Mobile-friendly interface
- Clean and intuitive user experience
- Consistent styling across all pages

### Dynamic Content
- Real-time room availability
- Status updates and notifications
- Interactive forms and validation

## 📈 System Benefits

### For Students
- **Convenience**: 24/7 online booking system
- **Transparency**: Real-time status tracking
- **Efficiency**: Reduced waiting times
- **Accessibility**: Mobile-friendly interface

### For Faculty
- **Streamlined Approval**: Centralized request management
- **Better Oversight**: Comprehensive booking overview
- **Reduced Workload**: Automated notification system
- **Data Analytics**: Booking patterns and usage statistics

### For Institution
- **Resource Optimization**: Better room utilization
- **Cost Reduction**: Reduced manual processes
- **Audit Compliance**: Complete booking history
- **Scalability**: Easy system expansion

## 🔮 Future Enhancements

### Planned Features
- **Calendar Integration**: Google Calendar synchronization
- **Mobile App**: Native mobile application
- **Advanced Analytics**: Usage reports and insights
- **Email Notifications**: Automated email alerts
- **Payment Integration**: Online payment processing
- **Multi-language Support**: Internationalization

### Technical Improvements
- **API Documentation**: Swagger/OpenAPI documentation
- **Unit Testing**: Comprehensive test coverage
- **Performance Optimization**: Caching and optimization
- **Security Enhancements**: JWT authentication
- **Database Optimization**: Indexing and query optimization

## 📊 Project Statistics

- **Total Files**: 25+ source files
- **Lines of Code**: 1000+ lines
- **Database Collections**: 7 collections
- **API Endpoints**: 15+ endpoints
- **User Interfaces**: 19+ pages
- **Dependencies**: 8 core packages

## 🏆 Technical Achievements

- **Full-stack Development**: Complete web application
- **Database Design**: Efficient MongoDB schema
- **Authentication System**: Secure session management
- **Responsive Design**: Mobile-friendly interface
- **Modular Architecture**: Clean code organization
- **Error Handling**: Comprehensive error management

## 📝 Documentation

The project includes comprehensive documentation:
- **SRS Document**: Software Requirements Specification
- **API Documentation**: Endpoint descriptions
- **Database Schema**: Collection structures
- **Installation Guide**: Setup instructions
- **User Manual**: Feature explanations

## 🎯 Conclusion

TARMS represents a modern, efficient solution for managing auditorium and room bookings in educational institutions. The system successfully addresses the challenges of manual booking processes while providing an intuitive, secure, and scalable platform for both students and faculty. With its robust architecture, comprehensive features, and user-friendly interface, TARMS sets a new standard for institutional resource management systems.

---

**Project Status**: ✅ Complete and Functional  
**Last Updated**: 2025  
**Version**: 1.0.0  
**License**: ISC


