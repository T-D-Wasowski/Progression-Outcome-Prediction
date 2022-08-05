def main():
    progressPrediction()

def progressPrediction():

    progessCount = 0
    trailerCount = 0
    excludeCount = 0
    retrieverCount = 0

    passed, deferred, failed = collectInput()
    
    volumes = [passed, deferred, failed]

    if rangeCheck(volumes) and totalCheck(volumes):
        
        if passed == 120:
            print("Progression outcome: Progress")
            progressCount += 1
            
        elif passed == 100:
            print("Progression outcome: Progress - module trailer")
            trailerCount += 1
            
        elif failed >= 80:
            print("Progression outcome: Exclude")
            excludeCount += 1
            
        else:
            print("Progression outcome: Do not progress - module retriever")
            retrieverCount += 1


def rangeCheck(l): #l - list, c - count, i - index

    c = 0

    for i in l:
        if i%20 == 0:
            c += 1
        else:
            continue
    
    if c == 3:
        return True
    else:
        print("Range Error: Please enter your credits within their valid ranges!")
        return False    

def totalCheck(l): #l - lsit

    if sum(l) == 120:
        return True
    else:
        print("Total Error: Please enter the correct volume of credits!")
        return False

def collectInput(): #p - passed, d - deferred, f - failed

    while True:
        
        try:
            p = int(input("Please enter volume of credits at Pass level: "))
            d = int(input("Please enter volume of credits at Defer level: "))
            f = int(input("Please enter volume of credits at Fail level: "))

            return p, d, f
        
        except ValueError:
            print("Data Type Error: Please ensure that you insert a valid integer!")

main()





    
    
