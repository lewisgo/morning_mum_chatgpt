import openai
from twilio.rest import Client
import datetime
import random

# Set up your OpenAI GPT-3.5 API key
openai_api_key = 'YOUR_OPENAI_API_KEY'

# Set up Twilio credentials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'
mom_phone_number = 'MOM_PHONE_NUMBER'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# List of love message starters
love_message_starters = [
    "Good morning, Mom! ",
    "Hello, Mom! ",
    "Hi Mom! ",
]

# Function to generate a love message using ChatGPT
def generate_love_message():
    prompt = random.choice(love_message_starters)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return prompt + response.choices[0].text.strip()

# Get today's date and format it
today_date = datetime.date.today().strftime('%Y-%m-%d')

# Generate a love message
love_message = generate_love_message()

# Create the message to be sent
message_body = f"{today_date}: {love_message}"

# Send the message
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=mom_phone_number
)

print(f"Message sent to Mom: {message.sid}")
