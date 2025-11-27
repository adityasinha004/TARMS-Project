const mongoose = require('mongoose');
const Faculty = require('./src/models/faculty');

mongoose.connect("mongodb://localhost:27017/test")
    .then(async () => {
        console.log("Connected to MongoDB");
        const faculty = await Faculty.find({});
        console.log("Faculty Users Found:", faculty);
        mongoose.disconnect();
    })
    .catch(err => console.error("Connection error:", err));
