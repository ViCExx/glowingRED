def greet(person, first_time=False):
    if first_time:
        return "First time, huh? Welcome, " + person
    return "Hello, " + person

def greet_all(people):
    for person in people:
        print(greet(person, True))

friends = ["JP", "Joe", "Kappu"]
greet_all(friends)