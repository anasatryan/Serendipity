import json
stress_cause = input("Are you stressed?")
if (stress_cause == "yes"):
 stressor1 = input("Is your stress caused by negative thoughts?")
 while (stressor1 == "yes"):
    print("read motivational articles,read some books or watch movies!")
    break
 stressor2 = input("Are you mentally and physically overwoked?")
 while(stressor2 == "yes"):
    print("try meditating, take your supplements, promote rest and mental relaxation")
    break
 stressor3 = input("Are you stressed because of a disease?")
 while(stressor3 == "yes"):
    print("Seek medical help from a professional or ask for help from your family and friends")
    break
else:
    your_stressor = input("Please provide the reason that caused your stress!")
