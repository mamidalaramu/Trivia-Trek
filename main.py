from src.presentation import play_game


def display_available_topics(topics):
    """Display available topics to the user."""
    print("Available topics: ")
    for key, value in topics.items():
        print(f"{key}: {value}")


def get_selected_topic(topics):
    selected_topic = input(
        "Enter the number corresponding to the topic you want to choose: "
    )
    if selected_topic.isdigit():
        selected_topic = int(selected_topic)
        try:
            selected_topic_value = topics[selected_topic]
            return selected_topic_value
        except KeyError:
            print("The topic does not exist in the available topics.")
            return None
    else:
        print("Please enter a number.")
        return None


def select_topic():
    topics = {
        1: "General Knowledge",
        2: "Entertainment: Books",
        3: "Entertainment: Film",
        4: "Entertainment: Music",
        5: "Entertainment: Television",
        6: "Entertainment: Video Games",
        7: "Entertainment: Board Games",
        8: "Science: Computers",
        9: "Science: Mathematics",
        10: "Sports",
        11: "Geography",
        12: "History",
        13: "Animals",
        14: "Vehicles",
        "q": "exit",
    }

    display_available_topics(topics)
    selected_topic_value = get_selected_topic(topics)

    return selected_topic_value


def get_difficulty_level():
    difficulty_modes = {
        1: "easy",
        2: "medium",
        3: "hard",
    }

    difficulty = input(
        "What level of difficulty would you like? 1-> Easy 2-> Medium 3-> Hard "
    )

    if difficulty.isdigit():
        difficulty = int(difficulty)
        try:
            selected_difficulty = difficulty_modes[difficulty]
            return selected_difficulty
        except KeyError:
            print("The selected mode does not exist in the available options.")
            return None
    else:
        print("Please enter a number.")
        return None


def welcome_message():
    print("Welcome to the Trivia Trek!")


def start_quiz():
    """Start the quiz game."""
    welcome_message()
    while True:
        answer = input("Press y to play? (y/n): ").lower()
        if answer == "n":
            break
        elif answer != "y":
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
        if answer == "q":
            break
        difficulty = get_difficulty_level()
        selected_topic = select_topic()
        if selected_topic is not None:
            print(f"You have selected the following topic: {selected_topic}")
            print("Getting related questions .....")
            play_game(selected_topic, difficulty)


if __name__ == "__main__":
    start_quiz()
