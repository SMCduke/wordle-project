import random

word_list = ["apple", "berry", "charm", "daisy", "eagle"]

def get_feedback(guess, answer):
    """Provide feedback for a guess compared to the answer."""
    feedback = []
    answer_letters = list(answer)
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            feedback.append("🟩")
            answer_letters[i] = None
        else:
            feedback.append(" ")


