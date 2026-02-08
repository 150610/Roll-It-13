
while True:

    want_instructions = input("Do you want to see the instructions? ").lower()

    #check if the user says yes/no
    if want_instructions == "yes" or want_instructions == "y" :
        print("You said yes")
        break
    elif want_instructions == "no" or want_instructions == "n" :
        print("You said no")
        break
    else:
        print("Please answer yes/no")
        continue

print("Done")