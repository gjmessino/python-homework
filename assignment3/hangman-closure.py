def make_hangman(secret_word):
    guesses = []
    word_list = list("_" * len(secret_word))
    def hangman_closure(letter):
        guesses.append(letter)
        print("".join(word_list))
        if "".join(word_list) == secret_word:
            return True
        else:
            return False
    return hangman_closure

secret = input("What's the secret word? ")
game1 = make_hangman(secret)
lett = input("Guess a letter: ")
while game1(lett) == False:
    lett = input("Guess a letter: ")
    game1(lett)