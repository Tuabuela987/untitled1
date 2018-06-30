sentence = input("Dime algo: ")
nsentence = ""
for i in range(len(sentence)):
    if sentence[i] == "a" or sentence[i] =="e" or sentence[i] =="i" or sentence[i] =="o" or sentence[i] =="u":
        nsentence += "i"
    else:
        nsentence += sentence[i]
print(nsentence)
