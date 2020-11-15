import random

answerChoice=["Absolutely!", "Eh, no!", "50/50 chance"] 

print("Welcome to the Magic 8 Ball game—use it to answer your questions...") 

print("\n")

question = input("Ask me a question and I’ll help you out. \n\nType your question then press ENTER to find out the answer: \n") 

print("shaking.... \n" * 4) 

choice = random.choice(answerChoice)

print(choice)