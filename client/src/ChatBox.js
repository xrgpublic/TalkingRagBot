import React from "react";


function ChatBox ({userInput, botResponse}){

    //Get prompt and response from server
    //Use Button to update user input box immediately.
    //Use loading font for Bot Resp
    //Use SSE for response then update page

    let parsedResponse = '';
    if (botResponse !== undefined){
        parsedResponse = JSON.stringify(botResponse);
        parsedResponse = parsedResponse.substring(1, parsedResponse.length-1);
        parsedResponse = parsedResponse.replaceAll('\\\\n', '\n');
        parsedResponse = parsedResponse.replaceAll('\\n', '\n');
        parsedResponse = parsedResponse.replaceAll('\\"', '"');
        parsedResponse = parsedResponse.replaceAll('\\\\"', '"');
        parsedResponse = parsedResponse.replaceAll('"\\', '"');
        parsedResponse = parsedResponse.replaceAll('"\\\\', '"');
        console.log('parsed resp'+parsedResponse)
    }



    //returns ChatBox component
    return (<div style={{whiteSpace: "pre-wrap"}} className="conversation">
        <p  className="message user-message no-read-aloud" >{userInput}</p>
        <p  className="message bot-message" id="message bot-message">{parsedResponse}</p>
        
    </div>
    )
};


export default ChatBox;