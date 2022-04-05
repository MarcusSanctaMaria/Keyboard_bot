#Bugs
# will only work for valid input "d" and "p"
#invalid input triggers else statement but program does not ask for input again

#menu tso that use can choose either pickup or delivery

print("Do you want your order delivered or are you picking it up?")

print("For delivery ender d")
print("For pickup enter p")

delivery = input()

if delivery == "d":
    print("Delivery")

elif delivery == "p":
    print("pickup")

else:
    print("That was not a valid input")