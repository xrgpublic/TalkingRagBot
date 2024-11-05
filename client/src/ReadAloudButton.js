// ReadAloudButton.js
import React, { useEffect } from 'react';

const ReadAloudButton = ({ text, isReadAloudOn }) => {
    useEffect(() => {
        const updateAudio = () => {
            const audioElement = document.getElementById('ra-audio');
            const playerElement = document.getElementById('ra-player');

            if (window.readAloudInit) {
                audioElement.src = "";
                audioElement.load();

                if (isReadAloudOn) { // Only initialize if Read Aloud is on
                    window.readAloudInit(audioElement, playerElement);
                }
            } else {
                const scriptUrl = "https://assets.readaloudwidget.com/embed/";
                const scriptElement = document.createElement("script");
                scriptElement.onload = () => {
                    if (isReadAloudOn) { // Only initialize if Read Aloud is on
                        window.readAloudInit(audioElement, playerElement);
                    }
                };
                scriptElement.src = `${scriptUrl}js/readaloud.min.js`;
                document.head.appendChild(scriptElement);
            }
        };

        // Run the update whenever the text or `isReadAloudOn` prop changes
        updateAudio();

    }, [text, isReadAloudOn]);

    return (
        <div>
            <p>This is the text {text}</p>
            <div id="ra-player" data-skin="https://assets.readaloudwidget.com/embed/skins/default">
                <div 
                    className="ra-button" 
                    onClick={() => {
                        if (isReadAloudOn) { // Play audio only if Read Aloud is on
                            const audioElement = document.getElementById('ra-audio');
                            const playerElement = document.getElementById('ra-player');
                            window.readAloud(audioElement, playerElement);
                        }
                    }}
                >
                    <svg viewBox="0 0 80 100">
                        <polygon points="80,50 0,100 0,0 80,50" fill="#484848" />
                    </svg>
                    Listen to this article
                </div>
            </div>
            <audio 
                id="ra-audio" 
                data-lang="en-US" 
                data-voice="free" 
                data-key="20f8cf955c990f3e70d04b8394341933"
            ></audio>
        </div>
    );
};

export default ReadAloudButton;
