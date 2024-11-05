import React from "react";
import ChatBox from "./ChatBox.js"

export default function ChatBoxComponent ({chatNumber, promptArray, botResponseArray}) {
    
   let chatBoxArray = [] //Will store all previous convos and the most recent one

    //Render each chat convo for the session and push to chatBoxArray
    for (let i=0; i<chatNumber; i++){
        let chatBoxArrayKey = '';
        chatBoxArrayKey = ''+i;
        chatBoxArray.push(<ChatBox key={chatBoxArrayKey} userInput={promptArray[i]} botResponse={botResponseArray[i]} />);
    };

    //Returns ChatBoxComponenent component with chatBoxArray inside it
    return (
        <div className="chat-area">
            {chatBoxArray}          
        </div>
    );
    
};



