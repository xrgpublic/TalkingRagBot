import React, {useEffect} from "react";
import "./App.css";
import "./ChatBoxComponent.js";
import ChatBoxComponent from "./ChatBoxComponent.js";
import io from 'socket.io-client';
import ReadAloudButton from "./ReadAloudButton.js";
const socket = io.connect("http://localhost:8080");
//import WebSocket from 'websocket';

//import TextArea from "./TextArea.js";
function App() {
  const [counter, setCount] = React.useState(0);
  const [promptArray, setPromptArray] = React.useState([]);
  const [botResponseArray, setBotResponseArray] = React.useState([]);
  const [userText, setUserText] = React.useState('');
  const [readAloudText, setreadAloudText] = React.useState("Welcome to the page!");

  //Sends prompt to server
  useEffect(() =>{
    console.log('data promot '+promptArray[counter-1])
    socket.emit("send_message", promptArray[counter-1])
  },[promptArray, counter])

  //Gets response  from server
  useEffect(() => { 
    socket.on("receive_message", data =>{
      var shallowCopy = botResponseArray.slice();  //create shallow copy of promptArray
      shallowCopy.push(data) //push newest prompt onto new array with shallow copy of promptArray
      setBotResponseArray(shallowCopy)
      setreadAloudText(data)
    });
  },[botResponseArray, readAloudText]);
  


  //Function ran when 'Generate' Button is pressed
  //Function pushes user prompt to array.
  function pushToArray(promptInput) {
    console.log('ran input '+promptInput)
    //pushing newest prompt onto promptArray via slice method
    var shallowCopy = promptArray.slice();  //create shallow copy of promptArray
    shallowCopy.push(promptInput) //push newest prompt onto new array with shallow copy of promptArray
    setPromptArray(shallowCopy) //set 'promptarray' using the shallow copy with the latest prompt pushed onto it
    setCount(counter+1); //Updating counter
 };






 // Example of updating the text
 const updateText = () => {
  console.log('text')
     setreadAloudText("This is the updated content for the Read Aloud button!");
 };





 //Overrides default POST request.
 //Using this so page doesn't reload on every time user presses 'Generate' button and sends a POST to /sendPost
 const handleSubmit = (event) =>{
  event.preventDefault(); //stops default POST function.
  const form = event.target;
  console.log('form : '+form.userinput)
  const formData = new FormData(form);
  console.log('form Data: '+formData)
  const formJson = Object.fromEntries(formData.entries());
  console.log(formJson.userinput);
  pushToArray(formJson.userinput);
  setUserText('')
  console.log('new array'+promptArray)

       //<ReadAloudButton chatNumber={counter}/>
 };
 //Renders app.<TextArea setPrompt={setPrompt}/>
  return (
    <div className="App">
      <header className="App-header"></header>
        <div className="container">
          <div className="sidebar">
            <button className="new-chat-btn">New Chat<br/>(Under Construction)</button>
          </div>
          <div className="main-content">
              <ChatBoxComponent chatNumber={counter} promptArray={promptArray} botResponseArray={botResponseArray}/>
                <form onSubmit={handleSubmit} action="/" method="post" >
                <textarea className="input-box" name="userinput" placeholder="Type your message here..." onChange={(e) => setUserText(e.target.value)} value={userText}></textarea>
                    <input  className="generate-btn" type="submit" value="Generate"/>
                </form>
                <button onClick={updateText}>Update Text</button>
                <ReadAloudButton text={readAloudText} />
        </div>
        <div className="sidebar">
            <button className="new-chat-btn">Options<br/>(Under Construction)</button>
        </div>
          <p>Loading</p>
      </div>
    </div>
    
  );

};

export default App;
