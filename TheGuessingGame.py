import random 

generatedNumber = random.randint(1,50)
noOfTries = 0
falseTries = 0
guessedNumber = 0
while True:
    if (falseTries == 3):
        print ("You are too idiot to even try this game.")
        break

    try:
        guessedNumber = int(input("Enter Your Number: "))
        noOfTries +=1
    except Exception as e:
        falseTries +=1
        print("Put an Integer Bro")
        continue

    if guessedNumber >= generatedNumber+5:
        print ("Too High.")
    elif guessedNumber > generatedNumber:
        print("Go a bit lower")
    elif guessedNumber <= generatedNumber -5:
        print ("Too Low")
    elif guessedNumber < generatedNumber:
        print ("Go a bit higher")

        
    else:
        print (f"""
Congratulations....
You guessed the number in just {noOfTries} tries !!!
""")
        break