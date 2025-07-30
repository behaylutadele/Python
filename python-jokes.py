import random

def tell_joke():
    jokes = [
        "Why do Python programmers prefer dark mode? Because light attracts bugs!",
        "How does a computer get drunk? It takes screenshots.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do Java developers wear glasses? Because they don’t C#.",
        "What's a programmer’s favorite hangout place? The Foo Bar.",
        "Why did the Python programmer not respond to the foreign keys? Because he couldn’t relate.",
        "How do you comfort a JavaScript bug? You console it.",
        "Why did the function return early? It had a date with a 'null' pointer.",
        "What's the most used language in programming romance? Python—because it has 'self'.",
        "Why do programmers prefer iOS development? Because on Android, they can't find the 'byte'."
    ]

    joke = random.choice(jokes)
    print("\n💻 Here's your programming joke of the day:")
    print("😂", joke)

# Run the joke function
tell_joke()
