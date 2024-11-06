from telegram import Bot
import asyncio
# import time

# Replace with your bot token and channel chat ID
TELEGRAM_TOKEN1 = '7174447911:AAFXtzYPvq6PghPj-7rGBKd1ipIJSJHKVUM'
CHANNEL_ID1 = '-1002178025575'  # or use the actual chat ID
message = "this is binance deal"

# Asynchronous function to send a message
async def send_message(CHANNEL_ID,TELEGRAM_TOKEN,message):
    try:
        # Create a Bot instance
        bot = Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(chat_id=CHANNEL_ID, text=message)
        # print(message)
    except Exception as e:
        # print(f"An error occurred: {e}")
        message="error"
# Main loop to send a message every 10 seconds
async def ply(message):
    max_messages = 2  # Stop after 10 messages
    message_count = 0
    TELEGRAM_TOKEN1 = '7174447911:AAFXtzYPvq6PghPj-7rGBKd1ipIJSJHKVUM'
    CHANNEL_ID1 = '-1002178025575' 
    try:
        while message_count < max_messages:
            await send_message(CHANNEL_ID1,TELEGRAM_TOKEN1,message)
            message_count += 1
            # await asyncio.sleep(60*1)  # Wait for 10 seconds before sending the next message
    except KeyboardInterrupt:
        # print("Stopped by user")
        message="error"

# Run the main function in an event loop
if __name__ == "__main__":
    asyncio.run(ply(message))
