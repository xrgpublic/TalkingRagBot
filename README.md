# TalkingRagBot

## Overview
TalkingRagBot is an AI-powered assistant designed to offer interactive conversations with features like text-to-speech, database memory, and retrieval-augmented generation. This application combines real-time messaging with deep contextual understanding, making it a versatile AI companion.


# Table of Contents


1. [Overview](#overview)
2. [Features](#features)
3. [Diagrams](#diagrams)
4. [Quick Start](#quick-start)
5. [Setup and Installation](#setup-and-installation)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Database Setup](#database-setup)
   - [Starting the Application](#starting-the-application)
   - [Enabling Read Aloud with Piper Integration for Custom Voices](#enabling-read-aloud-with-piper-integration-for-custom-voices)
   - [Known Issues](#known-issues)
6. [Commands](#commands)
7. [Usage Examples](#usage-examples)
8. [Project Motivation](#project-motivation)
9. [Technologies Used](#technologies-used)
10. [Contribution](#contribution)
11. [License](#license)

---

This structure will make it easy for users to navigate through the README and find the information they need.

## Features
- **Text-to-Speech (TTS) with Read Aloud**: Integrated with the **Read Aloud** widget for text-to-speech functionality. Users can select a **Piper** AI voice from Read Aloud's options or add a custom Piper voice for more personalization.
- **Retrieval-Augmented Generation (RAG)**: Uses a Chroma vector database for recalling relevant context from past conversations.
- **Custom Memory Commands**: Stores personalized interactions for future reference.

## Diagrams
<p align="center">
  <img src="https://github.com/user-attachments/assets/aa583f32-28fe-4583-a984-5038a133bef2" />
<br>Fig 1. Talking Rag Bot Overview<br>
</p>

<p align="center">
    <img src="https://github.com/user-attachments/assets/bac45924-1a3b-4529-89c1-03475b2ceffc" />
<br>Fig 2. RAG Overview
</p>

## Quick Start
1. Clone the repository.
2. Install dependencies for frontend and backend.
3. Set up the database.
4. Start the application.


## Setup and Installation

### Prerequisites


### Prerequisites

- [Node.js and npm](https://nodejs.org/en/download/prebuilt-installer)
- [Python (version 3.12)](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Ollama](https://ollama.com/)
- [Rust (required for some dependencies)](https://rustup.rs/)
- **[Read Aloud Extension (optional)](https://chrome.google.com/webstore/detail/read-aloud-a-text-to-speech/hdhinadidafjejdhmfkjgnolgimiaplp)**: Install the Read Aloud widget (available as a Chrome extension) for TTS functionality
- **[Piper TTS (optional)](https://github.com/rhasspy/piper)**: Piper integration in Read Aloud allows users to choose or add custom voices

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
    cd ..
    cd server
    npm install
    ```

4. **Install AI dependencies**:
    ```bash
    cd ..
    cd LocalAI
    pip install -r requirements.txt
    ```

### Known Issues

- When running `pip install -r requirements.txt`, you might encounter a wheel installation failure. If this occurs, please run the following commands to resolve the issue:
    ```bash
    pip install --upgrade setuptools wheel
    pip install playsound
    ```


#### Database Setup
1. Run the following commands in your PostgreSQL environment to set up the required database and tables:
  ```sql
  CREATE USER mruser WITH PASSWORD 'isSuperCool' SUPERUSER;
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

- **`/read`**: Reads the content of a specified file directly from the command line.
- **`/recall <text>`**: Searches memory for responses related to the provided user prompt.
- **`/launch <website>`**: Launches a website related to the provided prompt.
- **`/forget`**: Removes the last conversation stored in memory.
- **`/switchdb`**: Switches the database context to `public_database`.
- **`/memorize <text>`**: Stores the provided text as a memory.
- **`/creatingFile <filename>`**: Creates a new file with the specified name.

## Usage Examples
```text
User: "/recall What's my name?"
Bot: "Your name is Mr. User, known online as [Redacted]."

User: "/launch 'Can you open Dominos pizza in my browser?'"
Bot: Opens Dominos website.
```

## Project Motivation
This project was a learning exercise, with a focus on functional exploration over production ready code. This was my first AI project and first React project.  My goals were to get a strong understanding of how to build a fullstack React application, learn how LLMs work, and learn what tools an AI will need to properly interact with the average person(when compared to an "AI power user"). This is why you will see sprinkles of a bunch of different tools, but nothing completely implemented.  I just wanted proofs of concepts that I can use as a foundation for when I make real consumer ready products.

## Technologies Used

- **Frontend**: React, CSS for styling
- **Backend**: Node.js, Python
- **Database**: PostgreSQL for conversation storage and memory management
- **Vector Database**: ChromaDB for managing embeddings
- **Real-Time Communication**: Socket.io for real-time message exchange
- **Text-to-Speech**: Read Aloud widget with Piper integration for custom voices
- **AI Model**: Ollama with LLaMA and heremes 3 8B as base models for conversation and nomic-embed-text for RAG

## Contribution
Contributions are welcome! Please fork this repository and submit a pull request if you have suggestions or improvements.

## License
This project is licensed under the MIT License.
