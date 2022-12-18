const express = require('express') // Import express module
var bodyParser = require('body-parser') // Import body-parser module
const mongoose = require('mongoose') // Import mongoose module

const mongoDb = 'mongodb://localhost:27017/dogs' // Create a variable for the MongoDB connection string
mongoose.connect(mongoDb, { useNewUrlParser: true, useUnifiedTopology: true }) // Set up default mongoose connection

const db = mongoose.connection // Get the default connection
const app = express()// Create an instance of express
app.use(bodyParser.urlencoded({ extended: false }))// Parse application/x-www-form-urlencoded
app.use(bodyParser.json())// Parse application/json

const port = 3000

const dogsSchema = new mongoose.Schema({ // Create a schema for dogs
    breed: String,
    name: String,
    age: Number
})
const Dog = mongoose.model('Dog', dogsSchema) // Create a model for dogs
/*const dogs = [
    { breed:"Jinbob", name: "Rex" },
    { breed:"Poodle", name: "Buddy" },
    { breed:"Labrador", name: "Max" },
    { breed:"Pug", name: "Bella" },
    { breed:"Bulldog", name: "Charlie" },
    { breed:"German Shepherd", name: "Lucy" },
]*/
app.listen(port, () => {
  console.log(`Server running on port ${port}`)
})

url = "http://localhost:3000/"
// Create a to home route
app.get('/', (req, res) => {
    const dogs = Dog.find((err, dogs) => {
        if (err) return console.error(err)
        console.log(dogs)
    })
    res.json(dogs)
})

// Create a route for about page
app.get('/about', (req, res) => {
    res.send('This is the about page')
})

// Create a route for contact page
app.get('/contact', (req, res) => {
    res.send('This is the contact page')
})

// Create a route for help page
app.get('/help', (req, res) => {
    res.send('This is the help page')
})

// Create a route for dogs page
app.get("/dogs/:id", (req, res) => {
    Dog.findById(req.params.id, (err, dog) => {
        if (err) return console.error(err)
        res.json(dogs[req.params.id - 1])
    })
})

app.post("/dogs/", (req, res) => {
    console.log(req.body)
    const dog = new Dog({
        breed: req.body.breed,
        name: req.body.name,
        age: req.body.age
    })
    dog.save((err, dog) => {
        if (err) return console.error(err)
        console.log({message: "Dog added successfully"})
        res.json(dog)
    })

})

app.put("/dogs/:id", (req, res) => {
    const filter = { _id: req.params.id }
    const update = { breed: req.body.breed, name: req.body.name, age: req.body.age }

    Dog.findByIdAndUpdate(filter, update, (err, dog) => {
        if (err) return console.error(err)
        console.log({message: "Dog edited successfully"})
        console.log({message: `Dog ${req.params.id} edited successfully`})
        res.json(dog)
    })


})

app.delete("/dogs/:id", (req, res) => {

    Dog.findByIdAndDelete(req.params.id, (err, dog) => {
        if (err) return console.error(err)
        console.log({message:  `Dog ${req.params.id} deleted successfully`})
        res.json({message:  `Dog ${req.params.id} deleted successfully`})
    })
    console.log(req.params.id)
})
