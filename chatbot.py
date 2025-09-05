import ollama

def main():
    print("Chatbot🤖 (Gemma-2B) (type 'exit' to quit)\n")

    messages = []  # keep conversation history

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})

        response = ollama.chat(
            model="gemma:2b",
            messages=messages
        )

        bot_reply = response["message"]["content"]
        print(f"Bot: {bot_reply}")

        # add bot response to history
        messages.append({"role": "assistant", "content": bot_reply})

if __name__ == "__main__":
    main()
