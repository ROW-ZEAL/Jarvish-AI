# Jarvis A.I.

Jarvis A.I. is a simple voice-controlled assistant implemented in Python using the SpeechRecognition library. It can perform tasks like opening applications, providing the time and date, and opening websites.

## Features

- **Voice Recognition:** Uses the SpeechRecognition library to recognize voice commands.
- **Time and Date:** Tells the current time and date upon request.
- **Application Launcher:** Opens applications like Notepad and Calculator.
- **Website Opener:** Opens predefined websites based on user commands.

## Requirements

- Python 3.x
- SpeechRecognition library (`pip install SpeechRecognition`)
- Pyaudio library (required by SpeechRecognition, can be installed using system package manager or `pip install pyaudio`)
- `webbrowser` library (standard library in Python)
- `subprocess` library (standard library in Python)

## Usage

1. Run the script by executing `python jarvis.py`.
2. Jarvis will greet you based on the time of day.
3. Jarvis will listen for your commands. You can say things like:
   - "Open Notepad"
   - "What's the time?"
   - "Open Google"

## Supported Commands

- **Open Application:** You can ask Jarvis to open applications like Notepad and Calculator.
- **Open Website:** Jarvis can open predefined websites like Google, Wikipedia, ChatGPT, and YouTube.
- **Time Inquiry:** Ask Jarvis for the current time.
- **Date Inquiry:** Ask Jarvis for today's date.
- **Exit Jarvis:** You can exit Jarvis by saying "Jarvis exit."

## Extending Functionality

- You can extend the functionality by adding more applications to the `open_application` function.
- You can also add more websites to the `sites` list for Jarvis to open.

## Contribution

Feel free to contribute to the project by adding new features, fixing bugs, or improving the existing code. Create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).

