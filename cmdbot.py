from bot_logic import BotLogic

def main():
    # Instantiate the bot logic
    bot_instance = BotLogic()

    # Standard greeting message
    print("Hello! How can I help you with your science questions ⚛️?")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Generate and print the bot's response
        bot_response = bot_instance.generate_response(user_input)
        print("Bot:", bot_response)
    
if __name__ == "__main__":
    main()
