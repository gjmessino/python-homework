def make_hangman(secret_word):
    def hangman_closure(letter):
        guesses = []
        hang_list = list("_" * len(secret_word))
        guesses.append(letter)
        print("".join(hang_list))
        indices = [ind for ind, character in enumerate(secret_word) if character == letter]
        for item in indices:
            hang_list[item] = letter
        if "".join(hang_list) == secret_word:
            return True
        else:
            return False
    return hangman_closure()

secret1 = input("Pick a secret word: ")
x = True
while x == True:
    guessed_let = input("Guess a letter ")
    secret1(guessed_let)