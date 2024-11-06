import requests

# Replace with your bot's token
token = '7174447911:AAFXtzYPvq6PghPj-7rGBKd1ipIJSJHKVUM'
# TELEGRAM_TOKEN = '7174447911:AAFXtzYPvq6PghPj-7rGBKd1ipIJSJHKVUM'
# CHANNEL_ID = '-1002178025575'

# Telegram API URL for getting updates
url = f"https://api.telegram.org/bot{token}/getUpdates"

# Send a GET request to the URL
response = requests.get(url)

# Print the JSON response
print(response.json())
