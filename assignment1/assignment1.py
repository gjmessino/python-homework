# Task 1: Hello
def hello():
    return "Hello!"
# Task 2: Greet with a Formatted String
def greet(name):
    return (f"Hello, {name}!")
# Task 3: Calculator
def calc (num1, num2, operator = "multiply"):
    try:
        if operator == "add":
            return num1+num2
        elif operator == "subtract":
            return num1-num2
        elif operator == "multiply":
            return num1 * num2
        elif operator == "divide":
            try:
                return num1/num2
            except ZeroDivisionError:
                return("You can't divide by 0!")
        elif operator == "modulo":
            return num1%num2
        elif operator == "int_divide":
            try:
                return num1//num2
            except ZeroDivisionError:
                return("You can't divide by 0!")
    except Exception:
        return("You can't multiply those values!")

# Task 4: Data Type Conversion
def data_type_conversion(val,name):
    try:
        if name == "str":
                new_data = str(val)
                return new_data
        elif name == "float":
                new_data = float(val)
                return new_data
        elif name == "int":
                new_data = int(val)
                return new_data
    except:
            return(f"You can not turn {name} into {val}")
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
    except:
        return ("Invalid data was provided.")
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
    new_title =[]
    title1 = title.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    for word in title1:
        word1 = word.capitalize()
        if little_words.index[word] != -1:
            word1 = word.lower()
        new_title.append(word1)
    return ' '.join(new_title)
#Task 9: Hangman, with more String Operations
def hangman(secret, guess):
    new_word = ""
    for i in range(len(secret)):
        ind = guess.find(secret[i])
        if ind != -1:
            new_word += secret[i]
        else:
            new_word += "_"
    return new_word
# Task 10: Pig Latin, Another String Manipulation Exercise
def pig_latin(phrase):
    try:
        phrase2 = phrase.split()
        final = []
        vowels = "aeiou"
        for word in phrase2:
            if word[0] in vowels:
                final.append(word + "ay")
            elif word[0] == "q" and word [1] == "u":
                final.append(word[2:] + "ay")
            else:
                start = ""
                i = 0
                while i < len(word) and word[i] not in vowels:
                    start += word[i]
                    i += 1
                final.append(word[i:] + start + "ay")
        return ''.join(final)
    except:
        print("Please input a string")
