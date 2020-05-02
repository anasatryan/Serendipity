def taking_medications():
    while True:
        test4word = input("How many medications do you have to take today?")
        try:
            test4num = int(input("From 1 to 10, how many hours have passed since you took your pills?"))
            if (test4num <= 3):
                print("You should wait more,it has been ", test4num, "hours since you took your pills")
            else:
                if (test4num) >= 3:
                    print("You are doing great,it has been ", test4num, "hours! You can take your pills now!")
        except ValueError:
            print("Error! This is not a number. Try again.")
        break


def reminder_to_take_a_break():
