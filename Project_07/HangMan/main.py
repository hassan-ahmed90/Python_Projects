from hangman_art import stages,logo
from hangman_words import word_list
import random
random_word=random.choice(word_list)
lives=6
dashes=""
for i in range(len(random_word)):
    dashes+="_"
print(logo)
print(random_word)
dashes_list=list(dashes)
def hang_man():
    global lives
    while lives>0 and "_" in dashes_list:
        print(f"Word to Guess {''.join(dashes_list)}")
        user_word=input("Guess the word?\n")
        if user_word in random_word:
            for index,letter in enumerate(random_word):
                if letter==user_word:
                    dashes_list[index]=user_word
            print("Correct guess")
        else:
            lives-=1
            print(f"Wrong guess you left {lives} lives left")
            print(stages[lives])
    if "_" not in dashes_list:
        print(f"Congratulations! You guessed the word: {''.join(dashes_list)}")
    else:
        print(f"Game Over! The word was: {random_word}")


hang_man()