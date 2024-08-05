from telethon import TelegramClient, events
import google.generativeai as genai
import logging


genai.configure(api_key="AIzaSyD_ICyLntqEPQ1d6Awaxa195wRu51_au8A")
#img = PIL.Image.open('path/to/image.png')

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

#response = model.generate_content(["how to make rice?"])
#print(response.text)






# Set up logging
logging.basicConfig(level=logging.INFO)

# Telegram API credentials
api_id = 27166309
api_hash = 'cd4adea07c043878b111cd345d5b2f67'


# Create a Telegram client
client = TelegramClient('session', api_id, api_hash)



async def main():
    # Login to the Telegram client
    await client.start()


    # Send a direct message to a user by their phone number
    # Uncomment the line below to actually send a message (make sure you have permission)
    #await client.send_message('+919199208167', 'Hello!')

    # Listen for incoming messages
    @client.on(events.NewMessage(incoming=True))
    async def handle_message(event):
        # Get the message text and sender ID
        message_text = event.message.message
        sender_id = event.message.sender_id

        # Print the message to the console
        logging.info(f"Received message: {message_text}")

        # Respond to the user using the OpenAI chatbot
        response = model.generate_content( message_text)
                    
        logging.info(f"Received message: {response.text}")
        await client.send_message(sender_id,response.text )
        

    # Run the event loop
    await client.run_until_disconnected()

# Run the main function
client.loop.run_until_complete(main())


