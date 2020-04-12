import json
stress_cause = input("Are you stressed?")
while (stress_cause == "yes"):
   stressor1 = input("Is your stress caused by negative thoughts?")
   if (stressor1 == "yes"):
    print("read motivational articles,read some books or watch movies!")
    break
   stressor2 = input("Are you mentally and physically overwoked?")
   if (stressor2 == "yes"):
    print("try meditating, take your supplements, promote rest and mental relaxation")
    break
   stressor3 = input("Are you stressed because of a disease?")
   if (stressor3 == "yes"):
    print("Seek medical help from a professional or ask for help from your family and friends")
    break
   else:
    stress_cause = input("Please provide the reason that caused your stress!")
    print(stress_cause)
with open('my_data.json', 'w') as f:
    json.dump(stress_cause, f)
