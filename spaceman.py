import random

# Open up the words.txt file, store in variable words_list, separate the words into a variable secret_word
def load_word():
    f = open('words.txt', 'r') #opens the file 'words.txt' in read mode 'r' and stores the file object in variable 'f'
    words_list = f.readlines() #reads all the lines from the file f into a list, where each element of the list is a line from the file. This list is stored in the variable words_list.
    f.close() #closes the file 'f'
    
    words_list = words_list[0].split(' ') #takes the first element of 'words_list' and splits into individual words based on spaces
    secret_word = random.choice(words_list) #picks a random word from the list and stores it in 'secret_word'
    return secret_word #returns the 'secret_word' effectively making it the output of 'load_word' function

print(load_word())

# Function checks if all the letters in secret_word are present in letters_guessed
def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
 
# Function to generate and return a string that represents the letters correctly guessed so far, underscores letters incorrect
def get_guessed_word(secret_word, letters_guessed):
    word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += '_'
    return word

 
    
#TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet



#def is_guess_in_word(guess, secret_word):
    # '''
    # A function to check if the guessed letter is in the secret word

    # Args:
    #     guess (string): The letter the player guessed this round
    #     secret_word (string): The secret word

    # Returns:
    #     bool: True if the guess is in the secret_word, False otherwise

    # '''
    #TODO: check if the letter guess is in the secret word


#def spaceman(secret_word):
    # '''
    # A function that controls the game of spaceman. Will start spaceman in the command line.

    # Args:
    #   secret_word (string): the secret word to guess.

    # '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost

#These function calls that will start the game
secret_word = load_word()
# spaceman(secret_word)