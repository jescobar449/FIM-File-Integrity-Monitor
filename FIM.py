# Jose Melquiades Escobar
# Cyber Security Intern
# Final Project - File Integrity Monitor
# TLT - Tomorrow's Leaders Today, Inc 501(c)(3)

import hashlib
import os


# function to get the hash of a file
# return the SHA-1 hash of the file
def hash_file(filename):
    # make hash object
    h = hashlib.sha1()

    # check to see if the file exists
    # if true, get the hash
    # if false, notify the user
    if os.path.exists(filename):
        # open file for reading in binary mode
        with open(filename, 'rb') as file:
            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                chunk = file.read(1024)
                h.update(chunk)

            # return the hash
            return h.hexdigest()
    else:
        return "the file does not exist"


# prompt the user for input
print("What would you like to do?")
print("1) create a baseline file")
print("2) run FIM system")
choiceCheck = False

# check to see the user input a possible choice
while choiceCheck == False:
    choice = input("Enter 1 or 2: ")
    if choice == "1" or choice == "2":
        choiceCheck = True
    else:
        print("")
        print("Try again, Enter 1 or 2: ")

# create/ overwrite a baseline.txt file
if choice == "1":
    f = open("baseline.txt", "w")
    f.write("a.txt \n")
    f.write(hash_file("confidential/a.txt"))
    f.write("\n")
    f.write("b.txt")
    f.write("\n")
    f.write(hash_file("confidential/b.txt"))
    f.close()

    print("")
    message = hash_file("confidential/a.txt")
    print("a.txt hash = " + message)
    message = hash_file("confidential/b.txt")
    print("b.txt hash = " + message)

# check for integrity
elif choice == "2":
    print("")

    # open baseline.txt and put the hashes into an array
    baselineHashes = []
    baselineHashes2 = []
    file = open("baseline.txt", "r")
    # add the hashes to an array
    for line in file:
        baselineHashes.append(line)
    # remove any new line characters from any array element
    for item in baselineHashes:
        baselineHashes2.append(item.replace("\n", ""))

    currentHashes = []
    currentHashes.append(hash_file("confidential/a.txt"))
    currentHashes.append(hash_file("confidential/b.txt"))

    # notify user the baseline hashes
    print("------------------------")
    print("baseline hashes are: ")
    for item in baselineHashes2:
        print(item)
    print("")
    # notify user the current hashes
    print("current hashes are: ")
    for item in currentHashes:
        print(item)
    print("")

    # notify user if the baseline matches the current hashes
    print("------------------------")
    integrityCheckA = False
    integrityCheckB = False
    if baselineHashes2[1] != currentHashes[0]:
        if currentHashes[0] == "the file does not exist":
            print("Error detected: " + baselineHashes[0].replace("\n", "") + " was moved or deleted")
        else:
            print("Error detected: " + baselineHashes2[0].replace("\n", "") + " was altered")
        print("Action required: Integrity needs correction")
        print("")
    else:
        integrityCheckA = True
    if baselineHashes2[3] != currentHashes[1]:
        if currentHashes[1] == "the file does not exist":
            print("Error detected: " + baselineHashes[2].replace("\n", "") + " was moved or deleted")
        else:
            print("Error detected: " + baselineHashes2[2].replace("\n", "") + " was altered")
        print("Action required: Integrity needs correction")
        print("")
    else:
        integrityCheckB = True
    if integrityCheckA == True & integrityCheckB == True:
        print("All elements match.")
        print("Integrity is maintained.")
