def make_hangman(secret_word):
    guesses = []
    hang = str("_" * len(secret_word))
    def hangman_closure(letter):
        nonlocal guesses
        guesses.append(letter)
        if letter in secret_word:
            hang[secret_word.find(letter)] = letter
        print(hang)
        if guesses in secret_word:
            return True
        else:
            return False
    return hangman_closure(hangman_closure(input("Guess a letter: ")))

make_hangman(input("Pick a secret word: "))