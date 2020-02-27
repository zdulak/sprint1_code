import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


jim_question = ["Are you below 14? ", "Are you going to use a sauna? ", "Are you student? ", "Are you man? "]
jim_answer = [
    "Below the age of 14, usage of the gym is forbidden", "You need to pay 1500 HUF",
    "You need to pay 300 HUF", "You need to pay 750 HUF", "You need to pay 500 HUF"
    ]

jokes = [
    "A programmer's wife asks: Would you go to the shop and pick up a loaf of bread? And if they have eggs, get a dozen. \
The programmer returns home with 12 loaves of bread. They had eggs.",
    "Debugging is like being the detective in a crime drama where you are also the murderer",
    "Programming is like sex. One mistake and you have to support it for the rest of your life.",
    "!false (It’s funny because it’s true.)"
    ]


print("Welcome to our gym!")

pos = 0
while pos < len(jim_question):
    answer = input(bcolors.FAIL + jim_question[pos] + bcolors.ENDC)
    print(random.choice(jokes))
    if answer.lower() == "yes":
        print(bcolors.OKGREEN + jim_answer[pos] + bcolors.ENDC)
        break  # alternatywa: pos = len(jim_question); continue
    elif answer.lower() == "no":
        pos += 1
        if pos == len(jim_question):
            print(bcolors.OKGREEN + jim_answer[pos] + bcolors.ENDC)
    else:
        print("Please give answer yes or no")
