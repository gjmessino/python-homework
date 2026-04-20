def make_hangman(secret_word):
    guesses = []
    not_guessed = True
    hang_list = list("_" * len(secret_word))
    new_letter = input("Guess a letter: ")
    def hangman_closure(letter):
        nonlocal guesses
        nonlocal not_guessed
        nonlocal hang_list
        guesses.append(letter)
        indices = [ind for ind, character in enumerate(secret_word) if character == letter]
        for item in indices:
            hang_list[item] = letter
        print(str(hang_list))
        if "".join(hang_list) == secret_word:
            not_guessed = False
            return True
        else:
            return False
    return hangman_closure(new_letter)

secret = input("Pick a secret word: ")
make_hangman(secret)