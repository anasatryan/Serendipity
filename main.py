import json
import time
import webbrowser
import datetime

def main():
    menu()

def menu():
    print("Welcome to SERENDIPITY!")
    print("****MAIN MENU****")
    print("We can suggest the following options to help you!!")
    print()

    choice = input ("""
    A: Check your stress level
    B:Find out some useful tips for reducing your stress
    C:Tracker for your medications
    D:Take a break and enjoy some music with our reminder

    Please choose one of the options:""")

    if choice == "A" or choice =="a":
        display_stress_level()
    elif choice == "B" or choice =="b":
        display_stress_types()
    elif choice == "C" or choice =="c":
        taking_medications()
    elif choice =="D" or choice =="d":
        reminder_to_take_a_break()
    else:
        print("You must only select the provided options")
        print("Please try again!")
        menu()

def stresslevelinfo():

    with open('stress_level.json')as data_file:
        stress_level = json.load(data_file)
    return stress_level

def stresstypeinfo():

    with open('stress_types.json')as data_file:
        stress1 = json.load(data_file)
    return stress1

def display_stress_level():
        stress_level = int(input("Please enter your stress level"))
        while (stress_level <= 50):
            print("Your stress level is low")
            break
        else:
            while (stress_level <= 75):
                print("Your stress level is medium")
                break
            else:
                while (stress_level <= 100):
                    print("Your stress level is high")
                    break
        stress_level_storage = []
        stress_level_storage.append(stress_level)
        print(stress_level_storage)
        with open('mydata.json', 'w') as f:
            json.dump(stress_level_storage, f)


def display_stress_types():

        stress1 = stresstypeinfo()
        stress_types = input("Have you been stressed lately?")
        for key, item in stress1.items():
            user_stress = input(item["question"])
            if (user_stress.lower() == "yes"):
                print(item["recommendation"])
                webbrowser.open(item["article"])
                break
        else:
            print("Please have a good day and enjoy this playlist!")
            webbrowser.open("https://youtu.be/u1kHo3nnWP4")
        with open('my_data.json', 'w') as f:
            json.dump(stress_types, f)


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

 total_breaks = 3
 break_count = 0

 print("Please take a break and enjoy this playlist")
 currentDT = datetime.datetime.now()
 print (str(currentDT))

 while (break_count < total_breaks):
     time.sleep(10)
     webbrowser.open("https://youtu.be/YhdX0QuuJUQ")
     break_count = break_count + 1
     break



main()
print("Thank you for using our app!")
