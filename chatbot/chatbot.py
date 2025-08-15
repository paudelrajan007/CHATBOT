def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello there! How can I help you today?")
        
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")
        
        elif 'your name' in user_input:
            print("Chatbot: I'm a simple rule-based chatbot written in Python.")
        
        elif 'help' in user_input:
            print("Chatbot: Sure! You can ask me about myself, say hi, or say bye to exit.")
        
        elif 'bye' in user_input or 'exit' in user_input:
            print("Chatbot: Goodbye! Have a nice day. ")
            break
        
        else:
            print("Chatbot: I'm sorry, I don't understand that. Try asking something else.")

# Run the chatbot
chatbot()
