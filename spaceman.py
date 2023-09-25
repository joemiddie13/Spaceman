import random

# Open up the words.txt file, store in variable words_list, separate the words into a variable secret_word
def load_word():
    f = open('words.txt', 'r') #opens the file 'words.txt' in read mode 'r' and stores the file object in variable 'f'
    words_list = f.readlines() #reads all the lines from the file f into a list, where each element of the list is a line from the file. This list is stored in the variable words_list.
    f.close() #closes the file 'f'
    
    words_list = words_list[0].split(' ') #takes the first element of 'words_list' and splits into individual words based on spaces
    secret_word = random.choice(words_list) #picks a random word from the list and stores it in 'secret_word'
    return secret_word #returns the 'secret_word' effectively making it the output of 'load_word' function

# print(load_word())

# Function checks if all the letters in secret_word are present in letters_guessed
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

# test_secret_word = "dog"
# test_guessed_letters = ["f", "o", "l"]
#print(is_word_guessed(test_secret_word, test_guessed_letters))

 
# Function to loop through letters in secret word and build a string that shows letters correctly guessed
def get_guessed_word(secret_word, letters_guessed):
    word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += '_'
    return word
#print(get_guessed_word(test_secret_word, test_guessed_letters))
 
    
def spaceman(secret_word):
    letters_guessed = []
    wrong_guess = 0
    max_wrong_guess = 7
    game_over = False

    print("Welcome to the word guessing game, Spaceman!!!")
    print("<********************************************>")
    print("You will have seven attempts to guess the word correctly, inputting one letter at a time.")
    print("On each attempt, I will make sure you see how close you are getting!")
    print("Good luck!")

    while not game_over:
        guess = input("What letter do you guess? _")
        print(f"Letters used so far:{letters_guessed}")
        if len(guess) != 1:
            print("Please, only one letter at a time!")
        elif guess in letters_guessed:
            print("You already guessed this letter, try again!")
        elif guess in secret_word:
            letters_guessed.append(guess)
            print("Great guess!")
            print("Word: " + get_guessed_word(secret_word, letters_guessed))
            if is_word_guessed(secret_word, letters_guessed):
                print("Congrats! You guessed the correct word!")
                game_over = True
        else:
            letters_guessed.append(guess)
            wrong_guess += 1
            print("Sorry, that letter is not in the word.")
            print("Word: " + get_guessed_word(secret_word, letters_guessed))
            if wrong_guess == max_wrong_guess:
                print("You ran out of guesses. The word was " + secret_word + ".")
                game_over = True
        
        if game_over:
            play_again = input("Would you like to play again? Type: 'yes' or 'no': ")
            if play_again.lower() == "yes":
                secret_word = load_word()
                letters_guessed = []
                wrong_guess = 0
                game_over = False
            else:
                print("Thank you for playing S-P-A-C-E-M-A-N!!!!!")


    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)