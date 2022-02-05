def greet_all(people):
    for person in people:
        print("Hello " + person)
    
friends = ["JP", "Joe","Kappu"]
greet_all(friends)

#packing example below of the same thing, but with just the names and no worries about it being in a list.

def greet_all(*people): # the * at the begin. allows for us to pass without list
    for person in people:
        print("Hello " + person)
    
greet_all("JP", "Joe","Kappu")