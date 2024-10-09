# Basic chatbot using Python

def greet_user():
    """Function to greet the user."""
    return "Hello! I'm your friendly chatbot. How can I help you today?"

def farewell():
    """Function to say goodbye."""
    return "Goodbye! Have a nice day!"

def chatbot_response(user_input):
    """Function that provides responses based on user input."""
    # Basic responses based on keywords
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return "Hello! How can I assist you?"
    elif "how are you" in user_input.lower():
        return "I'm just a bunch of code, but I'm doing well! How about you?"
    elif "name" in user_input.lower():
        return "I don't have a name, but you can call me Chatbot!"
    elif "weather" in user_input.lower():
        return "I'm not sure about the weather right now, but you can check a weather app for accurate info."
    elif "bye" in user_input.lower() or "goodbye" in user_input.lower():
        return farewell()
    else:
        return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

def main():
    """Main function to run the chatbot."""
    print(greet_user())  # Initial greeting
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot: " + response)
        
        # Break the loop if user says 'bye'
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

if __name__ == "__main__":
    main()
