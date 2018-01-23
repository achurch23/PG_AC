import pyautogui as pg
import time
import webbrowser
points=0

# Question goes here
answer = pg.prompt(
"""
What is your spirit animal?

a)You are slow and lazy
b)you are really big and gray
c)you are multicolored and can blend in well

""")

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question goes here
answer = pg.prompt(
"""
Where do you like to be?

a)In rainforests in South America
b)You live in small groups all over africa and asia
c)you live trees in rainforests

""")

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
# Question goes here
answer = pg.prompt(
"""
What do you eat?

a)you eat leaves
b)twigs, tree bark, fruit, grasses, and small plants
c)cricket, mealworm, cockroach, grasshopper

""")

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question goes here
answer = pg.prompt(
"""
How do you mate?

a)you don't mate very often, but when you do you are very vocal
b)male elephants have to chase a female and stop her with his trunk
c)the female chooses who to mate with

""")

pg.alert("You chose " + answer)

# Answer and points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# End of survey
pg.alert("OK, here's your animal...")
#Sloth
if points <=5:
 pg.alert("You are a sloth")
 webbrowser.open("")
elif points >= 6 and points <= 7:
    pg.alert("You are an elephant")
elif points >= 8:
    pg.alert("You are a chameleon")
