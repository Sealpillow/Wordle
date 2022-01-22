import random

def generate_word():
    generate = open("word.txt").read().split()
    guess_word = random.choice(generate)
    return guess_word

def check(u,w):
    count = 0
    for i in range(5):
        if u[i] == w[i]:  # correct letter and position
            count += 1
    if count == 5:
        return True
    else:
        for i in range(5):
            if u[i] == w[i]:  # correct letter and position
                print(" "+u[i]+" ", end='')
            else:
                if u[i] in w:  # correct letter but wrong position
                    print("(" + u[i] + ")", end='')
                else:  # wrong letter and position
                    print(" # ", end='')
        print()
        return False
def checkvalid(s):
    generate = open("word.txt").read().split()
    if s in generate:
        return True
    else:
        print("Not in word list. Try again")
        return False
def checklength(s):
    length= len(s)
    if length != 5:
        print("Invalid word length")
    else:
        return True


def start_game():
    while True:
        s = input("Start the game?(y,n):").lower()
        if s != 'y' and  s != 'n':
            print("Invalid Input!")
        else:
            if s == 'y':
                return True
            else:
                return False

print("Instructions:")
print("Guess the WORDLE in 6 tries.")
print("Each guess must be a valid 5 letter word. Hit the enter button to submit.")
print("After each guess, the character will change to show how close your guess was to the word.")
print("Letter itself a - correct letter and position ")
print("Letter with brackets (a)- correct letter, wrong position ")
print("Hash tag # - wrong letter and position")
while True:
    ingame= start_game()
    if ingame:
        word = generate_word()
        print(word)
        for i in range(6):
            while True:
                print("Input:", end="")
                user = input().lower()
                if user == 'quit':
                    print("Thanks for Playing! Goodbye")
                    exit()
                count = checklength(user)
                if count:
                    break
            valid = checkvalid(user)
            if valid:
                status = check(user, word)
                if status:
                    print("Good Job! It's correct!")
                    break
            if i==5:
                print("Nice Try, better luck next time")
        print("The word is:"+word)
    else:
        print("Thanks for Playing! Goodbye")
        break
