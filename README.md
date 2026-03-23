# Jarvis Voice Assistant

An AI-powered desktop voice assistant built with Python and Eel. The project combines speech recognition, text-to-speech, face authentication, wake-word detection, automation utilities, and a browser-based desktop UI to create a Jarvis-style assistant for Windows.

## Overview

Jarvis starts a local Eel application, opens a desktop-style web UI, verifies the user with face authentication, and then listens for commands through either the microphone button or wake-word activation. Commands are processed in Python and routed to app launching, YouTube playback, WhatsApp automation, or a chatbot fallback.

## Features

- Voice command recognition with `SpeechRecognition`
- Spoken responses with `pyttsx3`
- Web-based desktop UI powered by `Eel`
- Face authentication using OpenCV
- Wake-word detection using Porcupine
- Open local applications and websites
- Play videos on YouTube
- Send WhatsApp messages, calls, and video calls
- Contact and command lookup with SQLite
- Chatbot fallback using HugChat

## Tech Stack

| Technology | Purpose |
| --- | --- |
| Python | Core backend logic |
| Eel | Bridge between Python and the web UI |
| HTML / CSS / JavaScript | Frontend interface |
| SpeechRecognition | Speech-to-text |
| pyttsx3 | Text-to-speech |
| OpenCV | Face authentication |
| Porcupine | Wake-word detection |
| PyAudio | Microphone input |
| SQLite | Commands and contacts storage |
| pyautogui | Desktop automation |
| pywhatkit | YouTube automation |
| HugChat | Chatbot integration |

## Architecture

The project uses a lightweight desktop-web architecture:

- `main.py` initializes Eel, starts the UI, and handles the startup authentication flow.
- `run.py` launches the assistant process and the wake-word listener in parallel.
- `engine/command.py` handles speech capture, command dispatch, and UI updates.
- `engine/features.py` contains feature implementations such as app launching, YouTube playback, WhatsApp automation, and chatbot calls.
- `engine/auth/` contains face recognition and training assets.
- `www/` contains the frontend files used by Eel.
- `jarvis.db` stores command and contact data.

## Project Structure

```text
TE(AI)- Mini Project/
├── engine/
│   ├── auth/
│   ├── command.py
│   ├── config.py
│   ├── cookies.json
│   ├── db.py
│   ├── features.py
│   └── helper.py
├── www/
│   ├── assets/
│   ├── controller.js
│   ├── index.html
│   ├── main.js
│   ├── script.js
│   └── style.css
├── contacts.csv
├── device.bat
├── error_log.txt
├── jarvis.db
├── main.py
├── run.py
└── README.md
```

## How It Works

1. The application starts and loads the Eel UI.
2. Face authentication verifies the user.
3. A background process listens for the wake-word.
4. After activation, Jarvis captures speech input.
5. Speech is converted to text using Google Speech Recognition.
6. The command is matched against supported actions.
7. If no direct command matches, the chatbot handles the request.
8. The response is spoken aloud and displayed in the UI.

## Getting Started

### Prerequisites

- Python 3.8+
- Windows OS
- Microphone
- Webcam
- Internet connection for speech recognition and chatbot responses

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Amisha65/Jarvis-AI-Assistance.git
cd Jarvis-AI-Assistance
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the required packages manually.

This repository does not currently include a `requirements.txt`, so install the libraries used by the project, such as:

```bash
pip install eel SpeechRecognition pyttsx3 opencv-contrib-python pvporcupine pyaudio pyautogui pywhatkit playsound hugchat
```

4. Run the application:

```bash
python run.py
```

## Notes

- The app is designed primarily for Windows.
- Speech recognition depends on an internet connection.
- WhatsApp actions are automated through the desktop app or URI handling, not an official API.
- Face recognition and wake-word features depend on local hardware and correct environment setup.

## Limitations

- No `requirements.txt` is included yet.
- Some automations are UI-based and may be sensitive to screen state or focus.
- The project currently contains duplicated files under the `AI/` directory in addition to the main runnable root files.
- Command understanding is mostly keyword-based.

## Future Improvements

- Add a proper `requirements.txt`
- Improve command parsing with intent classification
- Add offline speech recognition support
- Replace fragile UI automation flows with direct integrations where possible
- Clean duplicate project directories and training assets
- Improve packaging and installation steps

## License

This repository currently does not include a license file. Add one if you want to define how others may use the project.
