import vlc
import string
import time
# First, we will ask for the name of the user. We will take the user input
# using the input() method.
# After execution, the input() method takes the input from the user and
# returns a string.
# Next, we will select a word and ask the user to start guessing the
# characters in the word.
# We will also define the maximum number of attempts the user can take.
# Now, we will use a while loop to repeatedly ask the user to guess the
# character until the attempts are exhausted.
# Inside the while loop, if the user guesses the correct character.
# We will include it in the response. Otherwise, we will notify the user that
# they made a mistake.
# If the user is able to guess all the characters of the word within the
# maximum number of attempts, they win the game.
# If the user exhausts all their attempts before guessing the entire word,
# they lose.

# This just has all the pictures of the hangmans stored in a list
HANGMANPICS: list = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

obscured_list_word_guess = []


def get_indices(lst: list, targets: list):
    '''Take a list that you want to check and a target that check 
    what is in the lst and return the indexes of the target in the lst'''
    indices = []
    for target in targets:
        if target in lst:
            indices.append(lst.index(target))
    return indices


def unique_index(lst: list):
    oc_set = set()
    rest = []
    for index, value in enumerate(lst):
        if value not in oc_set:
            oc_set.add(value)
        else:
            rest.append(index)
    return rest


# ask for user name
user_name = input("What is your name: ")

# ask for the word that needs to be guessed
word_guess = input("Enter the word that needs to be guessed: ").lower()
for i in range(100):
    print()
list_word_guess = list(word_guess)

for char in list_word_guess:
    if char == " ":
        obscured_list_word_guess += " "
        continue
    elif char in string.ascii_letters or char in string.digits or char in string.punctuation:
        char = "."
        obscured_list_word_guess += char


# explain rules
print("You can only guess wrong 7 times until you die")
print("You can only put in one character at a time")
print("Punctuation is allowed and digits (i will probably change this) ")
count = 0


while True:
    # Guess the character that might be in the given word
    answer = input("Give a character: ")

    # the amount of characters you put in answer was more than 1
    if len(answer) > 1:
        print("You put in more the one character >:( ")
        continue

    # the character is in the word
    elif answer in word_guess:
        word_guess = word_guess.strip(" ")
        print(HANGMANPICS[count])
        print("that's in the word :) ")
        correct_sfx = vlc.MediaPlayer("C:\Personal Code\hangman\Video Game Coin Beep Sound Effect.mp3")
        correct_sfx.play()
        

        # replaces multiple characters at once that are the same
        if word_guess.count(answer) > 1:
            # replaces the first character of mutiple with the answer
            index = word_guess.index(answer)
            obscured_list_word_guess[index] = answer
            # replaces the rest
            result = unique_index(list_word_guess)
            for index in result:
                obscured_list_word_guess[index] = answer

        # only replaces character
        else:
            index = word_guess.index(answer)
            obscured_list_word_guess[index] = answer
        print(obscured_list_word_guess)
        if "." not in obscured_list_word_guess:
            print(f"{user_name} has won yippee :)")
            children_yay = vlc.MediaPlayer("C:\Personal Code\hangman\FNAF_ Kids Cheering - Gaming Sound Effect (HD).mp3")
            children_yay.play()
            time.sleep(4)
            break

    # the answer you gave was not in the word that needs to be guessed
    elif answer not in word_guess:

        # print losing message
        if count == 7:
            print("You have used all you chances you got executed")

            womp_womp = vlc.MediaPlayer(
                "C:\Personal Code\hangman\womp_womp.mp3")
            womp_womp.play()
            time.sleep(5)
            break

        print("You got it wrong Womp Womp :( ")
        print(HANGMANPICS[count])
        print(obscured_list_word_guess)
        getting_closer = vlc.MediaPlayer(
            "C:\Personal Code\hangman\Dawn of the first day -72 hours remain-.mp3")
        getting_closer.play()
        count += 1
