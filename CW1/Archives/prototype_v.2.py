p = int(input("Please enter credit volume at pass level: "))
f = int(input("Please enter credit volume at fail level: "))

reults = [p, f]

prog = "Progress"
progTrail = "Progress - Module Trailer"
noProg = "Do not Progress - Module Retriever"
ex = "Exclude"


outcomeDict = {
    [120, 0] : prog,
    [100, 20] : progTrail
    }

print(outcomeDict[[p,f]])
