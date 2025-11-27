const mongoose = require('mongoose');
const User = require('./src/models/user');

mongoose.connect("mongodb://localhost:27017/test")
    .then(async () => {
        console.log("Connected to MongoDB");
        const user = await User.findOne({ UserID: "102003001" });
        if (user) {
            console.log("Student user found:");
            console.log(`ID: ${user._id}`);
            console.log(`Name: ${user.Name}`);
            console.log(`UserID: ${user.UserID}`);
            console.log(`Password: ${user.Password}`);
            console.log(`Member_type: ${user.Member_type}`);
        } else {
            console.log("Student user NOT found!");
        }
        mongoose.disconnect();
    })
    .catch(err => console.error("Connection error:", err));
