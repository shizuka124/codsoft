def chatbot():
    print("Hello! I'm a chatbot. How can I help you today?")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a nice day.")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bot, but I'm functioning as expected. How about you?")
        elif 'your name' in user_input:
            print("Chatbot: I'm a simple rule-based chatbot created for demonstration.")
        elif 'what can you do' in user_input:
            print("Chatbot: I can answer simple questions and provide information based on predefined rules.")
        elif 'weather' in user_input:
            print("Chatbot: I can't check the weather right now, but you can look it up on a weather website or app.")
        elif 'joke' in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        elif 'programming language' in user_input:
            print("Chatbot: Some popular programming languages are Python, JavaScript, Java, and C++.")
        elif 'python' in user_input:
            print(
                "Chatbot: Python is a versatile programming language known for its readability and wide range of applications.")
        elif 'java' in user_input:
            print(
                "Chatbot: Java is a popular programming language, especially for building large-scale enterprise applications.")
        elif 'javascript' in user_input:
            print("Chatbot: JavaScript is widely used for web development, enabling interactive web pages.")
        elif 'c++' in user_input:
            print("Chatbot: C++ is an extension of C and is known for its performance and use in systems programming.")
        elif 'math' in user_input:
            try:
                expression = input("Chatbot: Enter a simple math expression (e.g., 2 + 2): ")
                result = eval(expression)
                print(f"Chatbot: The result is {result}")
            except:
                print("Chatbot: Sorry, I couldn't evaluate that expression.")
        elif 'date' in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}")
        elif 'time' in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}")
        elif 'thank you' in user_input or 'thanks' in user_input:
            print("Chatbot: You're welcome! If you have any other questions, feel free to ask.")
        elif 'bye' in user_input:
            print("Chatbot: Goodbye! Have a nice day.")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase your question?")


if __name__ == '__main__':
    chatbot()
