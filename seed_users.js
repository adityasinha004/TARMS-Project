const mongoose = require('mongoose');
const Faculty = require('./src/models/faculty');
const User = require('./src/models/user');

mongoose.connect("mongodb://localhost:27017/test")
    .then(async () => {
        console.log("Connected to MongoDB");

        // Default Faculty
        const faculty = {
            fac_name: "Dr. Ashima Singh",
            position: "Professor",
            uname: "admin",
            mob: 9876543210,
            Member_type: "faculty",
            eMail: "admin@thapar.edu",
            password: "admin"
        };

        // Default Student
        const student = {
            Name: "Aditya Sinha",
            UserID: "102003001",
            eMail: "student@thapar.edu",
            Member_type: "student",
            MobileNumber: 9876543211,
            DOB: new Date("2000-01-01"),
            Password: "123"
        };

        try {
            // Clear existing
            await Faculty.deleteMany({ uname: "admin" });
            await User.deleteMany({ UserID: "102003001" });

            // Create new
            await Faculty.create(faculty);
            await User.create(student);

            console.log("Users seeded successfully!");
            console.log("Faculty: admin / admin");
            console.log("Student: student@thapar.edu / 123");
        } catch (err) {
            console.error("Error seeding users:", err);
        } finally {
            mongoose.disconnect();
        }
    })
    .catch(err => console.error("Connection error:", err));
