def print_info(name, age, email):
    print(name + " is " + str(age) + ". Reached at " + email)

info = ["Arturo", 34, "wtfiam@me.org"]
print_info(*info)