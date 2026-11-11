import random
import hangman

stages = hangman.stages

counter = 0
word_list = ["xangrilots", "baguera", "dantossauro", "rabanete"]
placeholder = ""
correct_letters = []
incorrect = []

# Randomly choose a word from the word_list
list_items = (len(word_list))
random_item = random.randint(0, list_items - 1)
game_over = False

print(stages[counter])

# Ask the user to guess a letter and check which position is right or wrong

while not game_over and counter != 6:
    letter_guessed = input("Guess a letter: ").lower()
    placeholder = ""
    for letter in word_list[random_item]:
        if letter == letter_guessed:
            placeholder += letter
        elif letter in correct_letters:
            placeholder += letter
        else:
            placeholder += "_"
    if letter_guessed not in word_list[random_item]:
        incorrect.append(letter_guessed)
        counter += 1
    
    if letter_guessed in word_list[random_item]:
        correct_letters.append(letter_guessed)
        
    print(stages[counter])
    print(placeholder)
    print(f"Incorrect letters {incorrect}")
    print(f"Correct letters:  {correct_letters}")
    
    
    if "_" not in placeholder:
        game_over = True
        print("You win.")
            
    elif counter == 6:
        game_over = False
        print("Game over.")
        