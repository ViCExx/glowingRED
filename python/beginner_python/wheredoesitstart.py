import math
age = 34
print(len(str(id(str(age)) + math.floor(2.6))))

#brokendown
import math
age = 34
age_str = str(age)
id_age_str = id(age_str)
other = math.floor(2.6)
added = id_age_str + other
added_str = str(added)
length = len(added_str)
print(length)


print(len(str(id(str(age)) + math.floor(2.6))))
