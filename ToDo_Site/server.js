//var db = require('./database_handler.js')
const express = require('express');
const db = require('./db')
//const {DatabaseSync} = require('node:sqlite')
//const database = new DatabaseSync('database.db')
const path = require('path');
const app = express();
const PORT = 3000;
//const index = require ('./index');
//const {spawn} = requrie('child_process');
//const python_process = spawn('python3 ')
//import initSqlJs from 'sql.js';

function test(){
    return 1;
}
console.log(test());

function jsonToUl(data){
    const list = document.createElement('ul');
    list.setAttribute('id', 'taskList');
    data.forEach()
    const headers = Object.keys(data[0]);


}

//const insert = database.prepare('INSERT INTO data (key, value) VALUES (?,?)');

//insert.run(1,'hello');
///insert.run(2,'world');


//const escpos = require('escpos');
// install escpos-usb adapter module manually
//escpos.USB = require('escpos-usb');
// Select the adapter based on your printer type
//const device  = new escpos.USB();
// const device  = new escpos.Network('localhost');
// const device  = new escpos.Serial('/dev/usb/lp0');

//const options = { encoding: "GB18030" /* default */ }
// encoding is optional

//const printer = new escpos.Printer(device, options);


app.use(express.json());
app.use(express.urlencoded({extended:true}));

app.get('/', (req, res) => {
    //const query = database.prepare('SELECT * FROM tasks');

    //console.log(query.all());
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.post('/api/clicked', async (req, res) => {
    
    console.log("clicked");
    //const selectRes = await db.query('SELECT * FROM tasks');
    //console.log(selectRes.rows);
    //res.send(selectRes.rows);
    
})

app.post('/api/submit-form', async (req, res) => {
    //console.log(req)
    const taskName = req.body.taskName;
    const taskType = req.body.taskType;
    const taskPriority = req.body.taskPriority;
    const taskRecurring = req.body.taskRecurring;
    const insertQuery = 'INSERT INTO tasks(name, type, priority, recurring) VALUES($1, $2, $3, $4) RETURNING *';
    const insertValues = [taskName, taskType, taskPriority, taskRecurring]
    const insertRes = await db.query(insertQuery, insertValues);

    res.send(insertRes)
})

app.post('/api/tasks', async (req, res) => {
    try {
	//console.log("test");
        const insertQuery = 'SELECT * FROM tasks;';
        const responseRes = await db.query(insertQuery);
        //console.log(responseRes);
        res.send(responseRes);
    } catch (err) {
	//console.log("test2");
        console.error(err.message);
        res.status(500).send('Server Error');
    }

   })

app.post('/api/swapCompleted', async (req, res) => {
    try{
        //console.log(req.body.id);
        const swapQuery = 'UPDATE tasks SET completed = NOT completed where id = $1;';
        const swapValue = [req.body.id];
        const response = await db.query(swapQuery, swapValue);
        res.send(response)
    } catch (err){
        console.log(err.message);
        res.status(500).send('Server Error');
    }
})

app.post('/api/swapActive', async (req, res) => {
    try{
        const deactivateQuery = 'UPDATE tasks SET active = NOT active where id = $1;';
        const deactivateValue = [req.body.id];
        const response = await db.query(deactivateQuery, deactivateValue);
        res.send(response)
    } catch (err){
        console.log(err.message);
        res.status(500).send('Server Error');
    }
})

app.post('/api/deleteTask', async (req, res) => {
    try{
        const swapQuery = 'DELETE from tasks where id = $1;';
        const swapValue = [req.body.id];
        const response = await db.query(swapQuery, swapValue);
        res.send(response)
    }
    catch (err){
        console.log(err.message);
        res.status(500).send('Server Error');
    }
})
app.listen(PORT, '0.0.0.0', () => {
    console.log('Website live @ https://localhost:${PORT}');
});

