import random
from stages import render_stage
import json

class Hangman():

    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.user_answer = ['_'] * len(self.word)
        self.dashes = '-' * 30
        self.misses = 0
        self.MAX_MISSES = 6
        self.entered_letters = set()


    def print_header(self):
        print(self.dashes)
        print('\tH A N G M A N')
        print(self.dashes)

    
    def display_status(self):

        print('\nCurrent:', " ".join(self.user_answer))
        print(f'Hint: {self.hint}')
        print("Already Guessed:", ", ".join(sorted(self.entered_letters)))
        print(f'Misses: {self.misses} / {self.MAX_MISSES}')
        
    




    def process_guess(self, guess):

    

        if guess in self.entered_letters:
            print("You've already guessed that letter!")
        else:
            self.entered_letters.add(guess)


        if not guess.isalpha() or len(guess) != 1:
            print( "Invalid input! You can only enter alphabets (A-Z).")
            return


        if guess in self.word:

            for i, c in enumerate(self.word):

                if c == guess:
                    self.user_answer[i] = guess

            print("\nCorrect!")

        else:
            print("\nIncorrect!")
            self.misses += 1



    def play(self):

        
        self.print_header()

        while True:
            render_stage(self.misses)
            self.display_status()

            guess = input("\nGuess a letter: ").strip().upper()
            self.process_guess(guess)
            print(f'\n{self.dashes}')
           
            if self.is_won() or self.is_lost():
                render_stage(self.misses)
                self.display_result()
                break

            


    def is_won(self):
        return '_' not in self.user_answer
    
    def is_lost(self):
        return self.misses >= self. MAX_MISSES

    
    def display_result(self):
        if self.is_won():
            print(f'Word:', " ".join(self.user_answer) )
            print('You won!')
            print(self.dashes)

        if self.is_lost():
            print(f'Misses: {self.misses} / {self.MAX_MISSES}')
            print('You lose!')
            print(f'The word was: {self.word}')
    
    def print_goodbye(self):
        print(self.dashes)
        print("\tG O O D B Y E")
        print(self.dashes)



with open("words.json", "r") as f:
    words_list = json.load(f)

while True:

    selected = random.choice(words_list)

    word = selected["word"].upper()

    hint = selected["hint"]

    game = Hangman(word, hint)

    game.play()

    again = input("\nDo you want to play again? (Y/N): ").strip().upper()

    if again != "Y":
        game.print_goodbye()
        break
