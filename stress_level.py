import json
stress_level = int(input("Please enter your stress level"))
while(stress_level <= 50):
    print("Your stress level is low")
    break
else:
    while(stress_level<=75):
        print("Your stress level is medium")
        break
    else:
        while(stress_level<=100):
            print("Your stress level is high")
            break
stress_level_storage=[]
stress_level_storage.append(stress_level)
print(stress_level_storage)
with open('mydata.json', 'w') as f:
    json.dump(stress_level_storage, f)


