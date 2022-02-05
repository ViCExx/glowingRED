wtfiam = "Where am I?"

print(wtfiam[5])

#indexes: 1st character = 0 | -1 at the end

# string slicing

# the colon : is really what allows you to see past the intial index stopping point.4example.

wtfiam = "Where am I?"

print(wtfiam[4]) # prints the letter 'e'
print(wtfiam[4:]) # prints: e am I?
#
wtfiam = "Where am I?"

print(wtfiam[:5])
# the 5 on the right side, takes the chars from the left to right
#
# the 5 on the left side takes the chars from the right to the left.

wtfiam2 = "Where am I?!"

print(wtfiam2[:-2]) # this printed: Where am I
print(wtfiam2[:1]) # this printed: the W
print(wtfiam2[4:]) # this printed: e am I?!

# the first char on the left is 0
# the last char on the right is -1

wtfiam3 = "Where am I?"

print(wtfiam[-4:]) # printed: m I?
print(wtfiam3[6:]) # printed: am I?

"""
+---+---+---+---+---+
| P | y |t | h |o |n|
+---+---+---+---+---+
0   1   2  3   4  5  6
-6  -5  -4 -3  -2 -1 

slice and dice type functions that we can do to zone in on characters from the left or right, or both with say, numbers from [2:-2] would mean, the 0 1 2 postion of the value starting from the left. and the -2 would be the -1 -2 postion starting from the right. 

for example, in the real world, let says we have a list of serial numbers and they all start with XYZ<UNIQNE 3 DIGITS>999 - we would hone in on just the 3 digits, to find only, for example those that fell in the range of 200-497 due to the year they were made. maybe we are talking about cars, and these are engines. it can be anything. 

"""
name = "JoseLuis Alvarez"

start_of_last = 9
print(name[start_of_last:])
