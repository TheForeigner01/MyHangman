import random as r

guesses = []
word = "a"
ui = ""
fails = 0
lives = 10
wordlist = "wordlist.txt"
Found = False
Done = False
question = []
def welcome():
    print("___________________________________________________")
    print(" Welcome to hangman, this is a terminal-based game,\n you have to guess letters, just like in the original game.")
    p_choice = input("You can choose from 3 levels by typing the numbers: \n (1) - Easy \n (2) - Medium \n (3) - Hard \n ____________________________________________________\n \n")


    if int(p_choice) == 1:
        lvl_easy()
    elif int(p_choice) == 2:
        lvl_med()
    elif int(p_choice) == 3:
        lvl_hard()
    else:
        print("Invalid level of choice")
        welcome()

def lvl_easy():
    get_word()
    info()
    loop()
    
    
def lvl_med():
    print("med")

def lvl_hard():
    print("hard")


def get_word(): # gets random word from txt file
    global word
    global wordlist
    
    f = open(wordlist, "r")
    l = f.readlines()
    w_index = r.randint(0, len(l)-1)
    word = l[w_index].strip()

def info(): #shows information about the state of game for player
    print("You have guessed these letters so far:")
    print( *guesses, sep = ", ")
    print("\n" + ui)

    
def loop():
    global Done
    global lives
    global word
    global fails
    global question
    global answer
    answer = list(word)
    found = False

    while fails < lives:   
        
        n = 0
        while n < len(answer):
            question.append("_ ")
            n+=1

        if not Done:
            char = input("Guess a character frmóom the word: ")
            for i, asd in enumerate(answer):
                if asd == char:
                   question[i] = char
                   found = True

            if not found:
                fails += 1
        
            for i, asd in enumerate(question):
                w=0
                if asd != "_ ":
                    w+=1
                    if w == len(question):
                        win()
                        break

            print(question)
            #print(answer)
            print("number of fails: " + str(fails))
    print("You Lost")

def win():
    global Done
    Done = True
    print("You Won")

welcome()


