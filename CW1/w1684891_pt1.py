def main():

    while True:

        results = collectResults()

        if rangeCheck(results) and totalCheck(results):
            
            if results[0] == 120:
                print("Progression outcome: Progress")
                
            elif results[0] == 100:
                print("Progression outcome: Progress - module trailer")
                
            elif results[2] >= 80:
                print("Progression outcome: Exclude")
                
            else:
                print("Progression outcome: Do not progress - module retriever")

            break

        else:
            continue

def rangeCheck(l): #l - list, i - index

    for i in l:
        if i%20 == 0:
            continue
        else:
            print("Range Error: Please enter your credits within their valid ranges!")
            return False

    return True
    
def totalCheck(l): #l - lsit

    if sum(l) == 120:
        return True
    else:
        print("Total Error: Please enter the correct volume of credits!")
        return False

def collectResults(): #p - passed, d - deferred, f - failed

    while True:
        
        try:
            p = int(input("Please enter volume of credits at Pass level: "))
            d = int(input("Please enter volume of credits at Defer level: "))
            f = int(input("Please enter volume of credits at Fail level: "))

            return [p,d,f]
        
        except ValueError:
            print("Data Type Error: Please ensure that you insert a valid integer!")

main()





    
    
