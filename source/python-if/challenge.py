value = input("Would you like to continue? ")

if value == "y" or value == "yes" or value == "Yes":
    print("Continuing")
    print("Complete!")
elif value == "n" or value == "no" or value == "No":
    print("Exiting")
else:
    print("Please try again and respond with yes or no")
