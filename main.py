# Setup
from random import randint

q1 = "How long is the gestation period of an African elephant?"
a1 = "22 months"
q2 = "What’s the scientific name of a wolf?"
a2 = "Canis lupus"
q3 = "What is a female donkey called?"
a3 = "A Jenny"
q4 = "Which mammal has no vocal cords?"
a4 = "A giraffe"
q5 = "What’s the fastest land animal in the world?"
a5 = "The cheetah"
q6 = "How many eyes does a bee have?"
a6 = "Five"
q7 = "Which animal symbolizes good luck in Europe?"
a7 = "Ladybug"
q8 = "What name is used to refer to a group of frogs?"
a8 = "An army"
q9 = "How many hearts does an octopus have?"
a9 = "Three"
q10 = "Do sponges have hearts?"
a10 = "No"

# Title text
print()
print("Welcome to Mega Trivia!")
print("made by Miles")

# Spacing
print()
print()
print()
print()

for x in range(1, 10):
    num = [randint(1, 10) for p in range(1, 10)]
    print(num)