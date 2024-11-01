# TalkingRagBot

## Overview
MultiModalChatbot is an AI-powered assistant designed to offer interactive conversations with features like text-to-speech, database memory, and retrieval-augmented generation. This application combines real-time messaging with deep contextual understanding, making it a versatile AI companion.

## Features
- **Text-to-Speech (TTS) with Read Aloud**: Integrated with the **Read Aloud** widget for text-to-speech functionality. Users can select a **Piper** AI voice from Read Aloud's options or add a custom Piper voice for more personalization.
- **Retrieval-Augmented Generation (RAG)**: Uses a Chroma vector database for recalling relevant context from past conversations.
- **Custom Memory Commands**: Stores personalized interactions for future reference.

## Technologies Used

- **Frontend**: React, CSS for styling
- **Backend**: Node.js, Python
- **Database**: PostgreSQL for conversation storage and memory management
- **Vector Database**: ChromaDB for managing embeddings
- **Real-Time Communication**: Socket.io for real-time message exchange
- **Text-to-Speech**: Read Aloud widget with Piper integration for custom voices
- **AI Model**: Ollama with LLaMA and Hermès models for conversation, embeddings, and classification

## Setup and Installation

### Prerequisites

- Node.js and npm
- Python (version 3.8+)
- PostgreSQL
- **Read Aloud Extension (optional)**: Install the Read Aloud widget (available as a Chrome extension) for TTS functionality
- **Piper TTS (optional)**: Piper integration in Read Aloud allows users to choose or add custom voices

### Installation

Here’s the updated **README.md** with the revised list of commands, now that Vision is completely removed.

---

# MultiModalChatbot

This project is a robust web application designed as a user interface for an AI-powered assistant with multimodal capabilities, including text-to-speech (TTS) and retrieval-augmented generation (RAG).

## Features

- **Text-to-Speech (TTS)**: Integrated TTS capability for reading responses out loud.
- **Retrieval-Augmented Generation (RAG)**: Uses a Chroma vector database for conversational embeddings and efficient retrieval from past interactions.

## Technologies Used

- **Frontend**: React, CSS for styling
- **Backend**: Node.js, Python
- **Database**: PostgreSQL for conversation storage and memory management
- **Vector Database**: ChromaDB for managing embeddings
- **Real-Time Communication**: Socket.io for real-time message exchange
- **Speech Recognition and TTS**: Google Text-to-Speech and SpeechRecognition libraries
- **AI Model**: Ollama with LLaMA and Hermès models for conversation, embeddings, and classification

## Setup and Installation

### Prerequisites

- Node.js and npm
- Python (version 3.8+)
- PostgreSQL
- Install dependencies from `requirements.txt` and `package.json`.

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/xrgpublic/TalkingRagBot.git
    cd TalkingRagBot
    ```

2. **Install frontend dependencies**:
    ```bash
    cd client
    npm install
    ```

3. **Install backend dependencies**:
    ```bash
    cd..
    cd server
    pip install -r requirements.txt
    ```

#### Database Setup
1. Run the following commands in your PostgreSQL environment to set up the required database and tables:
  ```sql
  CREATE USER mruser WITH PASSWORD isSuperCool SUPERUSER;
  CREATE DATABASE memory_agent;
  GRANT ALL PRIVILEGES ON SCHEMA public TO mruser;
  GRANT ALL PRIVILEGES ON DATABASE memory_agent TO mruser;
  \c memory_agent
  CREATE TABLE conversations(
  id SERIAL PRIMARY KEY,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  prompt TEXT NOT NULL,
  response TEXT NOT NULL
  );
  INSERT INTO conversations (timestamp, prompt, response) VALUES (CURRENT_TIMESTAMP, 'What is my name?', 'Your name is Mr User. Known online as [Redacted].');
  ```

#### Starting the Application
1. In the main directory
```
# Run bat file
webui.bat
```
### Enabling Read Aloud with Piper Integration for Custom Voices

1. **Install Read Aloud**: Add the **Read Aloud** Chrome extension to your browser for TTS functionality.
2. **Enable Piper Voices**: Within Read Aloud’s settings, choose from existing Piper AI voices or add a custom voice by following the extension's guidelines for Piper integration.
3. **Select Your Voice**: In Read Aloud, configure your TTS settings to select your preferred Piper voice. Once configured, the chatbot will use the chosen voice for speech output when reading text aloud.

Using Read Aloud with Piper integration allows flexibility in voice options, enabling a more personalized assistant experience.

## Commands

The bot supports several commands for managing memory and performing specific tasks:
*Note*: The commands output only shows up in the CLI.

- **`/read`**: Reads a specified file’s content.
- **`/recall <text>`**: Retrieve related memories from past conversations.
- **`/launch <website>`**: Launches a website related to the provided prompt.
- **`/forget`**: Removes the last conversation stored in memory.
- **`/switchdb`**: Switches the database context to `public_database`.
- **`/memorize <text>`**: Stores the provided text as a memory.
- **`/creatingFile <filename>`**: Creates a new file with the specified name.

## Usage Example
```text
User: "/recall What is my name?"
Bot: "Your name is Mr. User, known online as [Redacted]."
```

## Project Motivation
This project was a learning exercise, with a focus on functional exploration over production ready code. This was my first AI project and first React project.  My goals were to get a strong understand of how to build a fullstack React application, learn how LLMs work, and learn what tools an AI will need to properly interact with the average person(when compared to an "AI power user"). This is why you will see sprinkles of a bunch of different tools, but nothing completely implimented.  I just wanted proofs of concepts that I can use as a foundation for when I make real consumer ready products.

## License
This project is licensed under the MIT License.
