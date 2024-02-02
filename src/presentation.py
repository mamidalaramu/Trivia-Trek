import random
from src.get_trivia import fetch_trivia_questions
from src.get_trivia import decode_trivia_questions

score = 0


def get_random_question():
    """Retrieve a random question from the decoded questions."""
    questions = decode_trivia_questions()
    return random.choice(questions)


def display_question(question):
    """Display a single trivia question and its options."""
    print(f"Question: {question['question']}")
    print("Options:")
    for idx, option in enumerate(question["options"], start=1):
        print(f"{idx}. {option}")


def get_user_answer():
    while True:
        user_input = input("Enter your answer (number): ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter a number.")


def check_answer(question, user_answer):
    """Check if user's answer is correct else provide correct answer."""
    global score
    correct_answer = question["correct_answer"]
    selected_option = question["options"][user_answer - 1]
    if selected_option == correct_answer:
        print("Correct! The correct answer is:", correct_answer)
        score += 1
        print(f"Correct! Your score is now: {score}")

    else:
        print("Incorrect! The correct answer is:", correct_answer)
        print(f"Your score remains: {score}")


def play_game(selected_topic, difficulty):
    fetch_trivia_questions(selected_topic, difficulty)
    """Start the trivia game."""
    while True:
        random_question = get_random_question()
        display_question(random_question)

        user_answer = get_user_answer()
        check_answer(random_question, user_answer)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Your total score is : ", score)
            print("Thank you for playing!")
            break
