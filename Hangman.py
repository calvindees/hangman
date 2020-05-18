#Setup/Variables
guesses_left = 7
win = 0
wordbank = ['python'] #add more words
incorrect_letters = []
correct_letters = []
allowed_inputs = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}


import random
chosen_word = random.choice(wordbank)

blank_spaces = ['_']*len(chosen_word)
#Opening Dialogue
print(f'Welcome to Hangman! The computer has automatically selected a word for you to guess. Your word is {(len(chosen_word))} letters long')
print(blank_spaces)
print(f'You have {guesses_left} guesses left')
print('What letter would you like to guess?')

while win == 0:

	if set(correct_letters) == set(chosen_word):
		print(f'Congrautlations, YOU WIN! The word was {chosen_word}')
		break
	guessed_letter = input()

	if guessed_letter not in allowed_inputs:
		print("That's not a valid guess!")
		

	elif guessed_letter in chosen_word:
		correct_letters.append(guessed_letter)
		allowed_inputs.remove(guessed_letter)
		print(f"Nice! '{guessed_letter}' is in the word, what would you like to guess next?")
		print(f'These letters are incorrect: {incorrect_letters}')
		print(f'These letters are correct: {correct_letters}')
		print(f'You have {guesses_left} guesses left')
		

	else:
		incorrect_letters.append(guessed_letter)
		guesses_left = guesses_left - 1
		allowed_inputs.remove(guessed_letter)
		print(f"Wah wah, '{guessed_letter}' is not in the word. Guess again!")
		print(f'These letters are incorrect: {incorrect_letters}')
		print(f'These letters are correct: {correct_letters}')
		print(f'You have {guesses_left} guesses left')
		if guesses_left == 0:
			print('YOU LOSE!') 
			break
		
	
		


	


