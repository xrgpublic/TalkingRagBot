const path = require('path');
const express = require("express");
const bodyParser = require('body-parser')
const cors = require('cors')
const http = require('http')
const { Server } = require('socket.io')




const PORT = process.env.PORT || 3001;

const app = express();

const server = http.createServer(app)

app.use(cors());
var prompt = 'empty'


app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json({ extended: false })) //This line allows react to send JSON to express

app.use(express.static(path.resolve(__dirname, '../client/build')));


//------------------WebSocket START------------------

const io = new Server(server, {
  cors:{
    origin: "http://localhost:3000",
    methods: ["GET","POST"],
  },
});

io.on("connection", (socket) => {

  console.log(`user connected: ${socket.id}`);

  socket.on("send_message", (data) => {
    prompt = JSON.stringify(data);
    socket.broadcast.emit("receive_message", data); //sends to everyone except person who sent it
  });
  socket.on('disconnect', () => {
    console.log(`user disconnected: ${socket.id}`);
   });
});

server.listen(8080, () => {console.log('Server is running on 8080');});

//------------------WebSocket END------------------

// All other GET requests not handled before will return our React app
app.get('*', (req, res) => {
  res.sendFile(path.resolve(__dirname, '../client/build', 'index.html'));
});

//App Listening on port 3001.  3001 is proxied to 3000.  See fccReact\client\package.json Line 5.
  app.listen(PORT, () => {
   console.log(`Server listening on ${PORT}`);
 });