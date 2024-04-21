import random

filename = 'values.txt'
def computerGuess(x):
    high = x
    low = 1
    noOfGuesses = 0
    reply = ''
    
    # This is to check the input value (reply) against certain specified keywords and to adjust the guess value 
    # accordingly
    
    while reply != 'c':
        if high != low:
            guess = random.randint(low, high)
            noOfGuesses = noOfGuesses + 1
        else:
            guess = low
        reply = (input(f"Is {guess} too high (H), too low (L), or correct (C)?: ").lower())
        if reply == 'h':
            high = guess-1
        elif reply == 'l':
            low = guess +1
    print(f"The computer guessed your number {guess} correctly in {noOfGuesses} tries!")
    
    # This part of the code is to write the guess and the no. of guesses to a separate .txt file.
    
    with open(filename, 'a') as file_object:
        file_object.write(str(guess))
        file_object.write(':')
        file_object.write(str(noOfGuesses))
        file_object.write('\n')


computerGuess(10000)