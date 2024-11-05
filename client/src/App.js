// App.js
import React, { useEffect, useState } from "react";
import "./App.css";
import ChatBoxComponent from "./ChatBoxComponent.js";
import io from 'socket.io-client';
import ReadAloudButton from "./ReadAloudButton.js"; // Importing the Read Aloud component
const socket = io.connect("http://localhost:8080");

function App() {
  const [counter, setCount] = React.useState(0);
  const [promptArray, setPromptArray] = React.useState([]);
  const [botResponseArray, setBotResponseArray] = React.useState([]);
  const [userText, setUserText] = React.useState('');
  const [readAloudText, setreadAloudText] = React.useState("Welcome to the page!");
  const [showReadAloudWidget, setShowReadAloudWidget] = useState(true); // Controls widget visibility
  const [highlightText, setHighlightText] = useState(false); // Controls text highlighting

  useEffect(() => {
    if (counter > 0) {
      socket.emit("send_message", promptArray[counter - 1]);
    }
  }, [promptArray, counter]);

  useEffect(() => {
    socket.on("receive_message", data => {
      const shallowCopy = [...botResponseArray];
      shallowCopy.push(data);
      setBotResponseArray(shallowCopy);
      
      // Update the read aloud text and reset highlighting if enabled
      setreadAloudText(data);
    });
  }, [botResponseArray]);

  function pushToArray(promptInput) {
    const shallowCopy = [...promptArray];
    shallowCopy.push(promptInput);
    setPromptArray(shallowCopy);
    setCount(counter + 1);
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    pushToArray(userText);
    setUserText('');
  };

  // Toggle visibility of the Read Aloud widget
  const toggleReadAloudWidget = () => {
    setShowReadAloudWidget(!showReadAloudWidget);
  };

  // Toggle text highlighting
  const toggleHighlightText = () => {
    setHighlightText(!highlightText);
  };

  return (
    <div className="App">
      <div className="container">
        <div className="sidebar">
          <button className="toggle-read-aloud-btn" onClick={toggleReadAloudWidget}>
            {showReadAloudWidget ? "Turn Read Aloud Off" : "Turn Read Aloud On"}
          </button>
          <button className="highlight-text-btn" onClick={toggleHighlightText}>
            {highlightText ? "Hide Highlight" : "Show Highlight"}
          </button>
        </div>
        <div className="main-content">
          <ChatBoxComponent 
            chatNumber={counter} 
            promptArray={promptArray} 
            botResponseArray={botResponseArray} 
            highlightText={highlightText} 
            readAloudText={readAloudText} 
          />
          <form onSubmit={handleSubmit} action="/" method="post" className="input-form">
            <textarea
              className="input-box"
              name="userinput"
              placeholder="Type your message here..."
              onChange={(e) => setUserText(e.target.value)}
              value={userText}
            />
            <button type="submit" className="generate-btn">
              ➤
            </button>
          </form>
          {showReadAloudWidget && (
      <ReadAloudButton text={readAloudText} isReadAloudOn={showReadAloudWidget} />
    )}
        </div>
      </div>
    </div>
  );
}

export default App;
