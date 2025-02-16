# NLP Personal Assistant

This project is a personal assistant application that uses natural language processing (NLP) to manage tasks such as reminders and user management.

## Features

- User authentication (login and logout)
- Role-based access control (Admin and User)
- Manage reminders
- Manage users (Admin only)

## Setup

### Prerequisites

- Python 3.7+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Werkzeug

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/nlp-personal-assistant.git
    cd nlp-personal-assistant
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the database:

    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. Create an admin user:

    ```sh
    python src/create_admin.py
    ```

### Running the Application

1. Start the Flask application:

    ```sh
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

### Usage

#### Logging in as Admin

1. Go to the login page.
2. Enter the admin email and password created during setup.
3. Click the login button.

#### Managing Users

1. After logging in as an admin, you will see a "Manage Users" button on the top of the chatbox.
2. Click the "Manage Users" button to go to the users management page.
3. On the users management page, you can see the list of users and add new users using the provided form.

### Project Structure

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