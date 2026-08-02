      #PROJECT : FAKE NEWS GENERATOR

Details=input("   Do you wanna generate FAKE NEWS ? (Yes/No)\n⚠️  CAUTION: This Program is just for fun.")

import random

subjects = ["Tanya","Ashwini","Simran","Lavanya","Virat","Rohit",""
"Dhoni","Sachin"]

Actions = ["Launches","cancels meeting ","dances with","eats","declare war on","orders","was Beaten"]

Places_or_things = ["at Red fort.","in Mumbai local train.","a plate of samosa.","inside Parliament.","at ganga ghat.","during IPL match.","at India gate."]

while True:

    if Details == "yes":
        print("\n----------------------------------\nWELCOME TO FAKE NEWS GENERATOR!!😁\n----------------------------------\nBased on your inputs:")
        # print("WELCOME TO FAKE NEWS GENERATOR!!😁")
        # print("----------------------------------")
        subject = random.choice(subjects)
        action = random.choice(Actions)
        place_or_thing = random.choice(Places_or_things)

        headline = (f"BREAKING NEWS: {subject} {action} {place_or_thing}")
        print("\n"+ headline)

        user_input = input("\nDo you want another headline? (Yes/No)")
        if user_input =="no":
         print("\nThanks for using the Fake News Headline Generator.Have a great Day.")
         break
    

    else:
        print("Thank you for your time.")
        break
    
    
    



    




    
