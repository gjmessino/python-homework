# Task 1: Diary
def diary():
    try:
        with open('diary.txt', 'a') as file:
            file.append(input("What happened today?"))
            done = False
            while done == False:
                new_line = file.append(input("What else?"))
                if new_line == "done for now":
                    done == True
                    file.close()
    except Exception as e:
        print(f"An exception has occured. {e}")
# Task 2: Read a CSV File
