import os
import random
import requests
import json
import base64

TRIVIA_FILE_PATH = "src/trivia_questions.json"


def fetch_trivia_questions(topic, difficulty):
    """
    Fetch trivia questions from the API based on the selected topic and difficulty and
    Save the questions to a JSON file.
    """

    if os.path.exists(TRIVIA_FILE_PATH):
        os.remove(TRIVIA_FILE_PATH)

    # Load category data from categories.json
    with open("src/categories.json", "r") as categories_file:
        categories_data = json.load(categories_file)

    # Find the category ID corresponding to the selected topic
    category_id = None
    for category in categories_data["trivia_categories"]:
        if category["name"] == topic:
            category_id = category["id"]
            break

    if category_id is None:
        print("Selected topic not found in available categories.")
        return

    # API URL Construction
    api_url = f"https://opentdb.com/api.php?amount=20&category={category_id}&difficulty={difficulty}&type=multiple&encode=base64"

    # Fetch trivia questions from the API
    response = requests.get(api_url)

    if response.status_code == 200:
        # Save response to a JSON file
        with open(TRIVIA_FILE_PATH, "w") as trivia_file:
            json.dump(response.json(), trivia_file, indent=4)
    else:
        print("Failed to get trivia questions.")


def decode_trivia_questions():
    """
    Decode trivia questions from the JSON file and prepare them for display.
    """
    decoded_questions = []

    # Read the JSON file containing Base64 encoded content
    with open(TRIVIA_FILE_PATH, "r") as trivia_file:
        trivia_data = json.load(trivia_file)

    # Decode and process each question in the API response
    for encoded_question in trivia_data["results"]:
        decoded_question = {}

        # Get decoded question and answer
        decoded_question["question"] = base64.b64decode(
            encoded_question["question"]
        ).decode("utf-8")
        decoded_question["correct_answer"] = base64.b64decode(
            encoded_question["correct_answer"]
        ).decode("utf-8")

        # Decode and shuffle incorrect answers
        decoded_question["incorrect_answers"] = [
            base64.b64decode(answer).decode("utf-8")
            for answer in encoded_question["incorrect_answers"]
        ]
        # Add correct answer to the list of options and shuffle them
        options = decoded_question["incorrect_answers"] + [
            decoded_question["correct_answer"]
        ]
        random.shuffle(options)
        decoded_question["options"] = options

        decoded_questions.append(decoded_question)

    return decoded_questions
