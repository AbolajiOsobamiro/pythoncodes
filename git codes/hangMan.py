import random
from words import words
import string


def getValidWords(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangMan():
    word = getValidWords(words)
    wordLetters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()
    lives = 7

    while len(wordLetters) > 0 and lives > 0: 
        print(f"You have {lives} lives left and you have used these letters", ' '.join(usedLetters))

        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current word: ', ' '.join(wordList))

        userLetter = input('Enter a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                print('You entered a wrong letter')
                lives = lives -1

        elif userLetter in usedLetters:
            print('You have already used that letter. Try again!')

        else:
            print('You entered an invalid character. Try again!')

    if lives == 0:
        print('[**********]Sorry, you died. The word was', word,'[********]'  )
    else:
        print('[#*#*#*#*#*]You guessed the word', word, '[#*#*#*#*#*]')
        
hangMan()




