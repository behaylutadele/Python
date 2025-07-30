def run_quiz():
    questions = [
        {
            "question": "What does 'len()' do in Python?",
            "options": ["A. Deletes a variable", "B. Returns the length", "C. Converts to string", "D. None of the above"],
            "answer": "B"
        },
        {
            "question": "Which movie features a character named Tony Stark?",
            "options": ["A. Batman", "B. Iron Man", "C. Spider-Man", "D. Superman"],
            "answer": "B"
        },
        {
            "question": "What keyword is used to define a function in Python?",
            "options": ["A. define", "B. def", "C. function", "D. lambda"],
            "answer": "B"
        },
        {
            "question": "Which animal is known as the king of the jungle?",
            "options": ["A. Elephant", "B. Lion", "C. Tiger", "D. Gorilla"],
            "answer": "B"
        },
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer was {q['answer']}.")

    print(f"\n🏁 You got {score}/{len(questions)} correct!")

def main():
    while True:
        run_quiz()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! 🎉")
            break

# Start the quiz
main()
