import random
import time

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) Bihar", "B) Chhattisgarh", "C) New Delhi", "D) Karnatak"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 3?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "C"
    }
]


def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)

def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer

def run_quiz():
    score = 0
    time_limit = 10  # Set time limit for each question (in seconds)
    
    random.shuffle(questions)  # Shuffle questions for randomness
    
    for q in questions:
        display_question(q)
        
        start_time = time.time()  # Start the timer
        user_answer = input(f"You have {time_limit} seconds to answer: ")
        
        elapsed_time = time.time() - start_time  # Calculate elapsed time
        
        if elapsed_time > time_limit:
            print("Time's up! You didn't answer in time.\n")
            continue  # Skip to the next question if time is exceeded
        
        if check_answer(user_answer, q["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    
    print(f"Your final score is {score}/{len(questions)}.")

run_quiz()