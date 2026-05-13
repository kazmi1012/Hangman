class Hangman():

    def __init__(self, word, hint):
        self.word = word
        self.hint = hint
        self.user_answer = ['_'] * len(self.word)
        self.dashes = '-' * 30

    def print_header(self):
        print(self.dashes)
        print('\nH A N G M A N')
        print(self.dashes)

    def process_guess(self, guess):

        if guess in self.word:

            for i, c in enumerate(self.word):

                if c == guess:
                    self.user_answer[i] = guess

            print("\nCorrect!")

        else:
            print("\nIncorrect!")

    def play(self):

        self.print_header()

        while True:

            print('\nCurrent:', " ".join(self.user_answer))
            guess = input("\nGuess a letter: ").strip().upper()
            self.process_guess(guess)
            print(f'\n{self.dashes}')
            if self.is_won():
                self.display_result()
                break

    def is_won(self):
        return '_' not in self.user_answer
    
    def display_result(self):
        if self.is_won():
            print(f'Word:', " ".join(self.user_answer) )
            print('You won!')
        self.dashes()



        


word = "PROGRAMMING"
hint = "The act of providing coded instructions to computers"

game = Hangman(word, hint)
game.play()
