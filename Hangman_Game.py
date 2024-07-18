import random
import Hangman_Stages
import word_list
print(f"{Hangman_Stages.welcome}\n\tYou have 6 lives to guess the correct word.\n")
game = input("Press 'Enter' to play or 'q' to Quit the game : ").lower()
if game != "q":
    #words = ["apple", "mango", "potato", "tomato", "banana", "desert", "pyspark", "python", "panda", "russia", "israel", "juicy"]
    lives = 6
    rand_word = random.choice(word_list.words)
    #print(rand_word)
#! Display "_" for randomly selected word.
    display = []
    for i in range(len(rand_word)):
        display += "_"
    print(display)
#! Guess letters present in random word.
    Game_Over = False
    while not Game_Over:
        guess_letter = input("Guess a letter : ").lower()
        for position in range(len(rand_word)):
            letter = rand_word[position]
            if letter == guess_letter:
                display[position] = guess_letter
        print(display)
        if guess_letter not in rand_word:
            lives -= 1
            if lives == 0:
                Game_Over = True
                print(f"You Loose! Game Over. The word is {rand_word}")
        if "_" not in display:
            Game_Over = True
            print("You won the Game")
        print(Hangman_Stages.stages[lives])
else:
    print("\n\t\tGame End")
