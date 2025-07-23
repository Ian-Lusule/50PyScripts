```python
"""
File: basic_quiz_game.py
Project: python-mini-projects

A simple quiz game with questions and answers.  The user's score is tracked and displayed at the end.
"""

import random

def load_questions(filepath="questions.txt"):
    """Loads quiz questions and answers from a text file.

    Args:
        filepath: The path to the question file.  Defaults to "questions.txt".

    Returns:
        A list of dictionaries, where each dictionary represents a question 
        with "question" and "answer" keys. Returns an empty list if the file 
        is not found or is empty.
    """
    try:
        with open(filepath, "r") as f:
            questions = []
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    question, answer = line.split(":", 1)  # Split at the first colon
                    questions.append({"question": question.strip(), "answer": answer.strip()})
            return questions
    except FileNotFoundError:
        print(f"Error: Questions file '{filepath}' not found.")
        return []


def play_quiz(questions):
    """Plays the quiz game.

    Args:
        questions: A list of question dictionaries.
    """
    if not questions:
        print("No questions loaded. Exiting.")
        return

    random.shuffle(questions)  # Shuffle questions for randomness
    score = 0
    num_questions = len(questions)

    print("Welcome to the Quiz Game!")

    for i, question_data in enumerate(questions):
        question = question_data["question"]
        answer = question_data["answer"].lower() #convert to lowercase for case-insensitive comparison

        print(f"\nQuestion {i+1}/{num_questions}: {question}")
        user_answer = input("Your answer: ").lower()

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")

    print(f"\nQuiz finished! Your score: {score}/{num_questions}")


if __name__ == "__main__":
    questions = load_questions()
    play_quiz(questions)

```

To use this code:

1.  **Create a `questions.txt` file:**  In the same directory as `basic_quiz_game.py`, create a text file named `questions.txt`. Each line in this file should contain a question and its answer, separated by a colon. For example:

    ```
    What is the capital of France?:Paris
    What is the highest mountain in the world?:Mount Everest
    What is the chemical symbol for water?:H2O
    ```

2.  **Run the script:** Execute `basic_quiz_game.py` from your terminal using `python basic_quiz_game.py`.


This improved version includes:

*   **Error Handling:**  The `load_questions` function handles the case where the `questions.txt` file is not found.
*   **Clearer Function Separation:** The code is divided into functions for better organization and readability.
*   **Case-Insensitive Answers:** The quiz now accepts answers regardless of capitalization.
*   **Random Question Order:** Questions are shuffled before the quiz begins.
*   **Documentation:** Docstrings explain the purpose of each function.
*   **Robustness:** Checks for empty question files and handles the case gracefully.


Remember to replace `"questions.txt"` with the actual path to your question file if it's located elsewhere.
