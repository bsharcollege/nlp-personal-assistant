# NLP Personal Assistant

This project is a Natural Language Processing (NLP) based personal assistant that can manage your calendar, answer FAQs, and interact with you through a web-based chat interface.

## Features

- **FAQ Management**: The assistant can answer frequently asked questions.
- **Calendar Management**: The assistant can create reminders and display them on a visual calendar.
- **Chat Interface**: Users can interact with the assistant through a web-based chat interface.

## Requirements

- Python 3.6+
- Flask
- nltk
- python-dateutil
- pytz
- requests
- spacy
- msal
- tkcalendar
- FullCalendar (JavaScript library)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/nlp-personal-assistant.git
    cd nlp-personal-assistant
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Download the spaCy language model:
    ```sh
    python -m spacy download en_core_web_md
    ```

## Usage

1. Start the Flask application:
    ```sh
    cd src
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Interact with the assistant through the chat interface. You can use commands like:
    - `add reminder to [subject] at [time] on [date]`
    - `show me reminder`
    - `show calendar`
    - `help`

## Example Commands

- `add reminder to go to office at 10:00 AM on 15 Feb`
- `show me reminder`
- `show calendar`
- `help`

## Project Structure

```
nlp-personal-assistant
├── src
│   ├── main.py               # Entry point of the application
│   ├── calendar_management.py # Manages calendar events
│   ├── faq.py                # Manages FAQs
│   ├── app.py                # Flask application
│   └── utils
│       └── __init__.py       # Utility functions
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Contributing

Feel free to submit issues or pull requests for improvements and features.