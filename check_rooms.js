const mongoose = require('mongoose');
const Rooms = require('./src/models/rooms');

mongoose.connect("mongodb://localhost:27017/test")
    .then(async () => {
        console.log("Connected to MongoDB");
        const rooms = await Rooms.find({});
        console.log("Rooms in database:");
        rooms.forEach(room => {
            console.log(`ID: ${room._id}, Number: ${room.Room_Number}, Name: ${room.Room_Name}, Status: ${room.Status}`);
        });
        mongoose.disconnect();
    })
    .catch(err => console.error("Connection error:", err));
