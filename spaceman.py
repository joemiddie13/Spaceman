import random #random module of the Python library generates random numbers for us

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

# Function to loop through letters in secret word and build a string that shows letters correctly guessed
def get_guessed_word(secret_word, letters_guessed):
    word = '' # empty string to capture letters and "_" underscores
    for letter in secret_word: # for loop iterates over each letter in the secret word
        if letter in letters_guessed: # check to see if player already guessed a correct letter
            word += letter # if true, letter is added to the 'word' string
        else:
            word += '_' # if 'letter' is not in 'letters_guessed' an '_' underscore is added to display string
    return word
 
# GAME TIME! 
def spaceman(secret_word):
    letters_guessed = [] # store the letters guessed by user
    wrong_guess = 0 # track the number of wrong 'letter' guesses
    max_wrong_guess = 7 # game ends after the 7th attempt
    game_over = False # control the game loop 

    print("Welcome to the word guessing game, Spaceman!!!")
    print("<********************************************>")
    print("You will have seven attempts to guess the word correctly, inputting one letter at a time.")
    print("On each attempt, I will make sure you see how close you are getting!")
    print("Good luck!")

    while not game_over: #continue this loop as long as the game is not over
        guess = input("What letter do you guess? _")
        print(f"Letters used so far:{letters_guessed}") # display the guessed letters used so far
        if len(guess) != 1: # ensure the player doesn't select more or less than one character
            print("Please, only one letter at a time!")
        elif guess in letters_guessed: # checks to see if they have guessed a letter more than once
            print("You already guessed this letter, try again!")
        elif guess in secret_word: # checks if guessed letter is in 'secret_word'
            letters_guessed.append(guess) # if correct, letter added to 'letters_guessed'
            print("Great guess!")
            print("You have " + str(max_wrong_guess - wrong_guess) + " turns left.")
            print("Word: " + get_guessed_word(secret_word, letters_guessed)) #invokes get_guessed_word to display current letters guessed correctly
            if is_word_guessed(secret_word, letters_guessed): # if all letters (word) is guessed correctly, game ends!
                print("Congrats! You guessed the correct word!")
                game_over = True
        else: # if letter_guessed is not in the secret_word
            letters_guessed.append(guess) # adds the incorrect letters_guessed
            wrong_guess += 1 # adds a 1 to the wrong_guess counter
            print("Sorry, that letter is not in the word.")
            print("You have " + str(max_wrong_guess - wrong_guess) + " turns left.")
            print("Word: " + get_guessed_word(secret_word, letters_guessed)) # invokes get_guessed_word to display current letters guessed correctly
            if wrong_guess == max_wrong_guess: # if player hits the 7th attempt and still not correct
                print("You ran out of guesses. The word was " + secret_word + ".")
                game_over = True
        
        if game_over: # Ask the player if they want to play again after a win or loss
            play_again = input("Would you like to play again? Type: 'yes' or 'no': ")
            if play_again.lower() == "yes":
                secret_word = load_word()
                letters_guessed = []
                wrong_guess = 0
                game_over = False
            else:
                print("Thank you for playing S-P-A-C-E-M-A-N!!!!!")

# Function calls that will start the game
secret_word = load_word()
spaceman(secret_word)