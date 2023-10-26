import random

# Define responses for the chatbot
responses = {
    "hello": ["Hi there!", "Hello!", "How can I help you today?"],
    "how are you": ["I'm just a computer program, but thanks for asking!", "I'm doing well, thanks!"],
    "goodbye": ["Goodbye!", "Have a great day!", "See you later!"],
    "default": ["I'm not sure what you mean. Can you please clarify?", "Sorry, I didn't understand that."]
}


def get_response(user_input):
    user_input = user_input.lower()

    # Check for specific keywords in the user's input
    if "hello" in user_input:
        return random.choice(responses["hello"])
    elif "how are you" in user_input:
        return random.choice(responses["how are you"])
    elif "goodbye" in user_input:
        return random.choice(responses["goodbye"])
    else:
        return random.choice(responses["default"])


def main():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()
