def main():

    outcomeCount = {
        "progress": 0,
        "trailer": 0,
        "exlude": 0,
        "retriever": 0
    }

    while True: #2
    
        while True: #1

            results = collectResults()

            if rangeCheck(results) and totalCheck(results):
                
                if results[0] == 120:
                    print("Progression outcome: Progress")
                    outcomeCount["progress"] += 1
                
                elif results[0] == 100:
                    print("Progression outcome: Progress - module trailer")
                    outcomeCount["trailer"] += 1
                    
                elif results[2] >= 80:
                    print("Progression outcome: Exclude")
                    outcomeCount["exclude"] += 1
                    
                else:
                    print("Progression outcome: Do not progress - module retriever")
                    outcomeCount["retriever"] += 1

                break #1

            else:
                continue

        choice = input("Press 'Q' to display outcome results and quit, or any other key to continue: ").lower()

        if choice == "q":
            print("Call funciton!!!")
            break #2
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





    
    
