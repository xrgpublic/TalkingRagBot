import React from "react";
import "./ChatBoxComponent.css";

const ChatBoxComponent = ({ promptArray, botResponseArray, highlightText, readAloudText }) => {
  const messages = [];
  const maxLength = Math.max(promptArray.length, botResponseArray.length);

  for (let i = 0; i < maxLength; i++) {
    if (i < promptArray.length) {
      messages.push({ sender: 'user', text: promptArray[i] });
    }
    if (i < botResponseArray.length) {
      messages.push({ sender: 'bot', text: botResponseArray[i] });
    }
  }

  return (
    <div className="chat-box">
      {messages.map((message, index) => (
        <div
          key={`${message.sender}-${index}`}
          className={`chat-message ${message.sender} ${highlightText && message.text === readAloudText && message.sender === 'bot' ? "highlight" : ""}`}
        >
          {message.text}
        </div>
      ))}
    </div>
  );
};

export default ChatBoxComponent;