const mongoose = require('mongoose');
const Rooms = require('./src/models/rooms');

mongoose.connect("mongodb://localhost:27017/test")
    .then(async () => {
        console.log("Connected to MongoDB");

        const rooms = [
            { Room_Number: "101", Room_Name: "Auditorium 1", Status: "Available" },
            { Room_Number: "102", Room_Name: "Auditorium 2", Status: "Available" },
            { Room_Number: "201", Room_Name: "Seminar Hall A", Status: "Available" },
            { Room_Number: "202", Room_Name: "Seminar Hall B", Status: "Booked" },
            { Room_Number: "301", Room_Name: "Conference Room", Status: "Available" }
        ];

        try {
            await Rooms.deleteMany({}); // Clear existing
            await Rooms.insertMany(rooms);
            console.log("Rooms seeded successfully!");
        } catch (err) {
            console.error("Error seeding rooms:", err);
        } finally {
            mongoose.disconnect();
        }
    })
    .catch(err => console.error("Connection error:", err));
