"""
This file is the entry point of the application. It initializes the NLP personal assistant and sets up the main loop for user interaction.
"""

from faq import FAQManager
from faq_data import FAQ_DATA
from calendar_management import CalendarManager
from datetime import datetime
import re
import requests

class NLPPersonalAssistant:
    def __init__(self):
        self.running = True
        self.faq_manager = FAQManager()
        self.calendar_manager = CalendarManager()
        self.setup_faqs()

    def setup_faqs(self):
        # Load FAQs from faq_data.py
        for question, answer in FAQ_DATA:
            self.faq_manager.add_faq(question, answer)

    def start(self):
        print("Welcome to your NLP Personal Assistant!")
        while self.running:
            user_input = input("How can I assist you today? ")
            response = self.process_input(user_input)
            print(response)

    def process_input(self, user_input):
        user_input = user_input.lower()
        if user_input in ["exit", "quit"]:
            self.running = False
            return "Goodbye!"
        elif "add reminder" in user_input:
            return self.create_reminder(user_input)
        elif "show reminder" in user_input:
            return self.show_reminders()
        elif "help" in user_input or "functions" in user_input:
            return self.show_help()
        elif "name" in user_input:
            return "Assistant: I am your NLP Personal Assistant."
        elif "hostel" in user_input:
            return "Assistant: Manipal University provides well-furnished hostels with various amenities for students."
        elif "weather" in user_input:
            return self.get_weather(user_input)
        else:
            answer = self.faq_manager.get_answer(user_input)
            if answer:
                return f"Assistant: {answer}"
            else:
                return "Assistant: I'm sorry, I don't understand that command."

    def create_reminder(self, user_input):
        # Parse the user input to extract reminder details
        match = re.search(r'add reminder to (.+) at (.+) on (.+)', user_input, re.IGNORECASE)
        if match:
            subject, time, date = match.groups()
            start_time = datetime.strptime(f"{date} {time}", "%d %B %Y %I %p").isoformat()
            reminder = self.calendar_manager.create_reminder(subject, start_time)
            return f"Assistant: Reminder '{subject}' created for {start_time}!"
        else:
            return "Assistant: Please provide the reminder details in the format: add reminder to [subject] at [time] on [date]"

    def show_reminders(self):
        reminders = self.calendar_manager.get_reminders()
        if reminders:
            response = "Assistant: Here are your reminders:\n"
            for reminder in reminders:
                response += f"- {reminder['subject']} at {reminder['start_time']}\n"
            return response
        else:
            return "Assistant: You have no reminders."

    def show_help(self):
        return (
            "Assistant: I can help you with the following functions:\n"
            "- Add a reminder: 'add reminder to [subject] at [time] on [date]'\n"
            "- Show reminders: 'show reminder'\n"
            "- Ask FAQs: 'what is your name?'"
        )

    def get_weather(self, user_input):
        match = re.search(r'weather in (.+)', user_input, re.IGNORECASE)
        if match:
            city = match.group(1)
            api_key = "your_api_key_here"  # Replace with your actual API key
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = data['weather'][0]['description']
                temperature = data['main']['temp']
                return f"Assistant: The weather in {city} is currently {weather} with a temperature of {temperature}°C."
            else:
                return "Assistant: I couldn't retrieve the weather information. Please try again later."
        else:
            return "Assistant: Please provide the city name in the format: weather in [city]"

if __name__ == "__main__":
    assistant = NLPPersonalAssistant()
    assistant.start()

