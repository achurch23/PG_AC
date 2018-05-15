import random

number = random.randint(0,3)

words = ["Koala","Dog","Fish", "Lizard"]

hint1 = ["australian","paws","gills", "reptile"]

hint2 = ["grey", "tail", "water", "green"]

guess = ""
counter = 1
secretword = words[number]

while True:
         print("guess the secret word!")
         print("Type 'hint1', 'hint2', 'first letter', 'last letter', or 'give up' for help.")
         guess = input()

         if guess == secretword:
            print("You win!")
            print("It took you " + str(counter) + "guesses.")
            break

         elif guess == "hint1":
             print(hint1[number] )

         elif guess == "hint2":
             print( hint2[number] )

         elif guess ==  "first letter":
             print( secretword[0] )

         elif guess == "last letter":
             print( secretword [-1] )

         elif guess == "give up":
             print( "The word was " + secretword)
             break

         else:
            print("Try again.")
            counter +=1


        
