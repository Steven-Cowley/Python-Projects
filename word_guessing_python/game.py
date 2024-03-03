# idea/help by app.dataquest.io
# link to what i was using here: https://www.dataquest.io/blog/python-projects-for-beginners/

# imports
import random
        
# variables
game_title = "word guess"

# holds the words used in the word bank
word_bank = []
# setting up in game variables
misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0

# opens word.txt and names it word_file
with open("words.txt") as word_file:
    # for each line within the word file: append the word to the list
    for line in word_file:
        word_bank.append(line.rstrip().lower())


# picking the random word in the word bank
word_to_guess = random.choice(word_bank)


# functions



# main program

# print the inital results
print("welcome to word guesser known as: " + game_title)
print("your word has ", len(word_to_guess), " letters")
print("you have ", max_turns - turns_taken, " guessses left")


# initalize the game loop
while turns_taken < max_turns:
    # get players guess
    guess = input("guess a word: ").lower()

    # check if the guess length is equal to 5 letters and has alpha characters
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("please enter a 5 letter word")
        continue

    # check each letter in the guess against the words letter
    index = 0
    # c becomes all letters in guess
    for c in guess:
        # check if the letters (c) is equal to the first index in the list (words to guess)
        if c == word_to_guess[index]:
            print(c, end=" ")
            # if any of the letters are incorrect
            if c in misplaced_guesses:
                # remove the letters from the list
                misplaced_guesses.remove(c)
        # if some letters are in the word to guess but not all
        elif c in word_to_guess:
            # TODO understand this: why append c in this situation???
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_", end=" ")
        # if none of the letter in the guess are in the word to guess
        else:
            # if the letter is not already in incorrect guesses
            if c not in incorrect_guesses:
                # letter gets added to incorrect guesses
                incorrect_guesses.append(c)
            print("_", end=" ")
        # compare the next letter in the list
        index += 1

        # print results to the user
        print("\n")
        print("misplaced letters: ", misplaced_guesses)
        print("incorrect letters: ", incorrect_guesses)
        turns_taken += 1

        # check if user has won
        if guess == word_to_guess:
            print("you win!")
            break

        # check if the player has lost
        if turns_taken == max_turns:
            print("you lose, the word wasL ", word_to_guess)
            break
        
        # display the number of turns left and ask for another guess
        print("you have ", max_turns - turns_taken, "turns left.")