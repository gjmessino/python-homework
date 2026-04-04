# Task 1: Hello
def hello():
    return "Hello!"
# Task 2: Greet with a Formatted String
def greet(name):
    return "Hello, " + name + "!"
# Task 3: Calculator
def calc (num1, num2, operator = "multiply"):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Pick a real number")
        return
    if operator == "add":
        return num1+num2
    elif operator == "subtract":
        return num1-num2
    elif operator == "divide":
        try:
            return num1/num2
        except ZeroDivisionError:
            print("These numbers cannot be divided")
    elif operator == "modulo":
        return num1%num2
    elif operator == "int_divide":
        try:
            return num1/num2
        except ZeroDivisionError:
            print("These numbers cannot be divided")
    else:
        return int(num1/num2)
# Task 4: Data Type Conversion
def data_type_conversion(val,name):
    if name == "str":
        try:
            new_data = str(val)
            return new_data
        except TypeError:
            print("Type Error")
    elif name == "float":
        try:
            new_data = float(val)
            return new_data
        except TypeError:
            print("Type Error")
    elif name == "int":
        try:
            new_data = int(val)
            return new_data
        except TypeError:
            print("Type Error")
    else:
        return
# Task 5: Grading System, Using *args
def grade(*args):
    try:
        ave = sum(args) / len(args)
        if ave >= 90:
            return "A"
        elif ave>= 80:
            return "B"
        elif ave>= 70:
            return "C"
        elif ave>= 60:
            return "D"
        else:
            return "F"
    except ZeroDivisionError:
        print ("Could not be divided")
# Task 6: Use a For Loop with a Range
def repeat (word, count):
    new_word = ""
    for i in range(count):
        new_word += word
    return new_word
# Task 7: Student Scores, Using **kwargs
def student_scores(posit, **kwargs):
    if posit == "mean":
        return sum(kwargs.values()) / len(kwargs)
    elif posit == "best":
        top_score = 0
        name = ""
        for k, v in kwargs.items():
            if v > top_score:
                top_score = v
                name = k
        return name
#Task 8: Titleize, with String and List Operations
def titleize(title):
    new_title = title.split()
    new_title = new_title.capitalize()
    for word in new_title:
        if word == "a" or "on" or "an" or "the" or "of" or "and" or "is" or "in":
            word.lower()
    return new_title.join()
#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    new_secret = ""
    for i in range (len(secret)):
        for k in range(len(guess)):
            if guess[k] == secret[i]:
                new_secret += guess[k]
            else:
                new_secret += "_"
    return new_secret
# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(phrase):
    sequence = phrase.split()
    new_phrase = []
    for words in sequence:
        if words[0] == "a" or "e" or "i" or "o" or "u":
            new_phrase.append(words + "ay")
        elif words[0] == "q" and words[1] == "u":
            new_phrase.append(words.slice(2) + "quay")
        else:
            new_word = ""
            while (words[0] != "a" or "e" or "i" or "o" or "u"):
                start += words [0]
                new_word = words.slice(1)
            words.append("ay")
            new_phrase.append(new_word + start + "ay")
        new_phrase += words
    return new_phrase
