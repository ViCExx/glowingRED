ages = [24, 34, 28, 25, 27, 35, 26, 36 ]
people = ["jp", "joe", "justin", "chris", "chase", "mason", "andrew", "pat" ]
fav_things = ["drones","traveling",['tarkov',
'plants', 'grilling']]
people[4] = "chaddyORTON"

fav_things = ["drones","traveling",['tarkov',
'plants', 'grilling']]
copy2 = fav_things[:]

print(fav_things[2][1]) #printing just the 2nd list 

print(copy2) #remember that 0 starts the list

#copy lists

fav_things = ["drones","traveling","football",['tarkov', 'plants', 'grilling']]
dupe = fav_things.copy()

print(fav_things, dupe)

####combining lists

fav_things.append("gambling")
print(fav_things)