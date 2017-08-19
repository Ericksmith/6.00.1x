numBobs = 0
i = 0


for i in range(len(s)):
    if (s[i:i+3]) == "bob":
        numBobs += 1

print("Number of times bob occurs is: " + str(numBobs))
