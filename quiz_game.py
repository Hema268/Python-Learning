print("Welcome to my Computer Quiz! ")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Lets play :) ")

answer = input("What does CPU stand for ? ")
if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does PUS stand for ? ")
if answer == "power supply":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What UI ? ")
if answer == "user interface":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for ? ")
if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does ux stand for ? ")
if answer == "user experience":
    print("Correct!")
else:
    print("Incorrect!")
