print("What is your name?")
nameofuser = input()
print("What are you looking for?")
answer = input()
FBImsg = "drugs"
FBImsg2 = "hentai"
wants = ["knowledge", "power", "money", "drugs", "hentai"]
if answer in {FBImsg,FBImsg2}: #did () and {} and it worked
    print(nameofuser + ", THIS IS THE FBI! GET ON THE GROUND!!!!")
else: 
    print("Thank you, for being a decent human being " + str(nameofuser))

#https://stackoverflow.com/questions/15112125/how-to-test-multiple-variables-for-equality-against-a-single-value

# I was looking for: if x == 1 or y == 1 or z == 1:they are all evaluated on their own. if 1 in (x,y,z): or better still if 1 in {x,y,z}:
# I'm sure there is a better way, but my whole goal was to have both drugs and hentai be flagged as the FBImsg - i couldn't get it until I created another variable with "hentai" and changed from and if answer: to if answer in {} or () <-- they both worked.
# making a note of it, because I spent a good 1-2 hrs working through it.

# the real question is, can i use one variable with differnt 'wants' and how do i make it to where it doesn't matter the case of the letters?