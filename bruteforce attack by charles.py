# CHARLES' BRUTFORCE ATTACK.....always use strong passwords
import sys
import os

# All possible characters.
characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
              "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`",
              "-", "=", "[", "]", "\\", ";", "'", ",", ".", "/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "~",
              "_", "+", "{", "}", "|", ":", '"', "<", ">", "?"]

password = input("Enter the password trying to be brute forced: ")

process = input("\nWould you like to display the process?\n\nNote: agreeing to display the process means the program will take a much longer time to run.\n\nSo, yes or no? ")

if process.lower() == "no":
    # Create an empty list to store the indexes of the characters in the password.
    indexes = []

    for character in password:
        index = 1
        for value in characters:
            if character == value:
                indexes.append(index)

            else:
                index += 1

    index = 1
    index2 = 0
    tries = 0
    for i in range(len(indexes) - 1):
        temp = (94 ** index) * indexes[index2]
        tries += temp
        index2 += 1
        index += 1

    tries += indexes[-1]

    print("\nThe password was guessed in", tries, "tries.")

elif process.lower() == "yes":
    guessed = characters
    tries = 0
    guess = 0
    estimates = []


    for character in characters:
        tries += 1

        if character == password:
            print("Password guessed in", tries, "tries.")
            sys.exit()

    temp = []
    loops = 0

    while guess != password:
        for value in guessed:
            # Loop through each character in the characters list.
            for character in characters:
                possibility = value + character
                tries += 1
                os.system('clear')
                print("Password:", password)
                print("Current Guess:", possibility, "\nTry Number", tries)
                if possibility == password:
                    print("\nPassword guessed in", tries, "tries.")
                    sys.exit()

                else:
                    temp.append(possibility)
        guessed = []
        guessed = temp
        temp = []

### random password generator ###
import random

desired_length = int(input())

random_output = []

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
              "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`",
              "-", "=", "[", "]", "\\", ";", "'", ",", ".", "/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "~",
              "_", "+", "{", "}", "|", ":", '"', "<", ">", "?"]

for iteration in range(desired_length):
    random_output.append(random.choice(characters))

print(*random_output, sep="")