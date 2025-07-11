print("""--->Fortnite addict Test<---
by: ilvi
""")
optionone = 0
optiontwo = 0
optionthree = 0
optionfour = 0
questionOne = int (input("""Do you like Fortnite?
1. I love it!
2. Yes
3. Maybe
4.No: """))
if questionOne == 1:
    optionone = optionone +1
elif questionOne == 2:
    optiontwo = optiontwo +1
elif questionOne == 3:
    optionthree = optionthree +1
elif questionOne == 4:
    optionfour = optionfour +1
else:
    print("Wrong input, try again")
questionTwo = int(input("""How often do you play fortnite at the weekend?
1. 48hrs
2. 24hrs
3. 12hrs
4. 0hrs
: """))
if questionTwo == 1:
   optionone = optionone +1
elif questionTwo == 2:
     optiontwo = optiontwo +1
elif questionTwo == 3:
  optionthree = optionthree +1
elif questionTwo == 4:
  optionfour = optionfour +1
else:
  print("Wrong input try again")
questionThree = int(input("""what was your highest level in Fortnite?
1. 200+
2. 100+
3. 50+
4. 0
: """))
if questionThree == 1:
    optionone = optionone +1
elif questionThree == 2:
    optiontwo = optiontwo +1
elif questionThree == 3:
    optionthree = optionthree +1
elif questionThree == 4:
    optionfour = optionfour +1
else:
    print("Wrong input try again")
print("Loading results...")
print("Results loaded")
print("Your results are:")
if optionone > optiontwo:
    print("You should get mental help")
elif optiontwo > optionthree:
  print("You are a Fortnite addict")
elif optionthree > optionfour:
  print("You are slightly addicted to Fortnite")
else:
  print("You are not addicted to Fortnite, you are a normal person congrats!")
print("Thank you for taking the quiz!")
