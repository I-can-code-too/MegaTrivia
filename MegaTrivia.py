import random

from MegaTriviaQuestion import TriviaQuestion

question_prompts = [
    "How long is the gestation period of an African elephant?\n(a) 5 Days\n(b) 1 Year\n(c) 22 Months\n\n",
    "What’s the scientific name of a wolf?\n(a) Canis Lupus\n(b) Oryctolagus Cuniculus\n(c) Vulpes Vulpes\n\n",
    "Which mammal is known to have the most powerful bite in the world?\n(a) Tiger\n(b) Hippopotamus\n(c) Raccoon\n\n",
    "What common farm animal doesn’t have teeth on their upper jaw?\n(a) Sheep\n(b) Pig\n(c) Cow\n\n",
    "How many dolphin species exist in the world?\n(a) 7\n(b) 120\n(c) 40\n\n",
    "A dog sweats through which part of its body?\n(a) Nose\n(b) Paws\n(c) Tail\n\n",
    "Butterflies use which part of their body to taste?\n(a) Wings\n(b) Feet\n(c) Tongue\n\n",
    "Where is a shrimp’s heart located in its body?\n(a) Head\n(b) Tail\n(c) Legs\n\n",
    "How many noses is a slug known to have?\n(a) 6\n(b) 1\n(c) 4\n\n",
    "Which mammal is not able to jump?\n(a) Rat\n(b) Buffalo\n(c) Elephant\n\n",
]

questions = [
    TriviaQuestion(question_prompts[0], "c"),
    TriviaQuestion(question_prompts[1], "a"),
    TriviaQuestion(question_prompts[2], "b"),
    TriviaQuestion(question_prompts[3], "a"),
    TriviaQuestion(question_prompts[4], "c"),
    TriviaQuestion(question_prompts[5], "b"),
    TriviaQuestion(question_prompts[6], "b"),
    TriviaQuestion(question_prompts[7], "a"),
    TriviaQuestion(question_prompts[8], "c"),
    TriviaQuestion(question_prompts[9], "c"),
]

random.shuffle(questions)

def run_trivia(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        else:
            print(f"The answer was: {question.answer}")
    print (f"You got {score} out of {len(questions)} correct")

run_trivia(questions)