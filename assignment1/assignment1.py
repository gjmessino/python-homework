# Task 1: Hello
def greeting():
    return "Hello!"
# Task 2: Greet with a Formatted String
def greeting2(name):
    return "Hello, " + name
# Task 3: Calculator
def calc (num1, num2, operator = "multiply"):
    try:
        num1 = int(num1)
        num2 = int(num2)
    if operator == "add":
        return num1+num2
    elif operator == "subtract":
        return num1-num2
    elif operator == "divide":
        return num1/num2
    elif operator == "modulo":
        return num1%num2
    elif operator == "int_divide":
        return num1/num2
    else:
        return num1*num2
# Task 4: Data Type Conversion
def data_type_conversion(val,name):
    if name == "str":
        return str(val)
    elif name == "float":
        return float(val)
    elif name == "int":
        return int(val)
    else:
        print("Improper value given")
        return
# Task 5: Grading System, Using *args
def grade(*args):
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
# Task 6: Use a For Loop with a Range
def repeat (word, count):
    for i in range(count):
        word = word + word
    return word
# Task 7: Student Scores, Using **kwargs
def student_scores(posit, **kwargs):
    if posit == "mean":
        return sum(kwargs.values) / len(kwargs)
    elif posit == "best":
        top_score = 0
        name = ""
        for k, v in kwargs.items:
            if v > top_score:
                top_score = v
                name = k
        return name
#Task 8: Titleize, with String and List Operations
def titleize(title):
    new_title = title.split()
    new_title = new_title.title()
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
def igpay_atinlay(phrase):
    phrase.split()
    new_phrase = ""
    for words in phrase:
        if words[0] == "a" or "e" or "i" or "o" or "u":
            words.append("ay")
        elif words[0] == "q" and words[1] == "u":
            words.slice(2)
            words.append("qu")
            words.append("ay")
        else:
            first = words [0]
            words.slice(1)
            words.append(first)
            words.append("ay")
        new_phrase += words
    return new_phrase