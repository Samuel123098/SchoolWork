dictonary = {}

Sentance = input("Please enter a sentance")
for i in range(len(Sentance)):
    if Sentance[i] in dictonary:
        dictonary.pop(Sentance[i])