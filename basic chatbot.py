from datetime import datetime
from zoneinfo import ZoneInfo

print("Chatbot: Hello! I am your chatbot. Type 'bye' or 'exit' to end the conversation.")

while True:
    user_input=input("You: ").lower()

    if"hello"in user_input or"hi"in user_input:
        response = "Hello! How can I assist you today?"

    elif "how are you" in user_input:
        response = "I'm fine thanks for asking. How can I help you?"

    elif "your name" in user_input:
        response = "I have no name till now."
        
    elif "help" in user_input:
        response = "I can assist with basic questions. Try asking about my name or how I am."

    elif "bye" in user_input or "exit" in user_input:
        response = "Goodbye! Have a great day!"
        print(f"Chatbot: {response}")
        break

    elif "time" in user_input:
        now = datetime.now(tz=ZoneInfo("Asia/Kolkata"))
        response = f"The current time is {now.strftime('%H:%M:%S')}."

    elif "date" in user_input:
        today = datetime.today()
        response = f"Today's date is {today.strftime('%Y-%m-%d')}."

    else:
        response = "I'm sorry, I didn't understand that. Can you please rephrase?"

    print(f"Chatbot: {response}")
