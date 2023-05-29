print("Hi, I'm a Chatbot. How can i help you ?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["hi", "hello", "hey"]:
        print("Chatbot: Hello! How can I help you today?")
    elif user_input.lower() == "what's your name?":
        print("Chatbot: My name is Chatbot")
    elif user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: Have a great day, bye.")
        break
    else:
        print("Chatbot: I'm sorry. I don't understand what you are saying. Can you rephrase that?")
