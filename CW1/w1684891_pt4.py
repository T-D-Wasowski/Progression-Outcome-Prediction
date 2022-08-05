def main():

    print("Welcome to the progression outcome predictior!")

    outcomeCount = {
        "Progress": 0,
        "Trailer": 0,
        "Exclude": 0,
        "Retriever": 0
    }

    for i in range(10):
    
        while True: 

            results = predefinedResults(i)

            if rangeCheck(results) and totalCheck(results):
                
                if results[0] == 120:
                    print("\nProgression outcome: Progress")
                    outcomeCount["Progress"] += 1
                
                elif results[0] == 100:
                    print("\nProgression outcome: Progress - module trailer")
                    outcomeCount["Trailer"] += 1
                    
                elif results[2] >= 80:
                    print("\nProgression outcome: Exclude")
                    outcomeCount["Exclude"] += 1
                    
                else:
                    print("\nProgression outcome: Do not progress - module retriever")
                    outcomeCount["Retriever"] += 1

                break 

            else:
                continue

    displayOutcomesExtension(outcomeCount)       

def rangeCheck(l): #l - list, i - index

    for i in l:
        if i%20 == 0:
            continue
        else:
            print("\nRange Error: Please enter your credits within their valid ranges!")
            return False

    return True
    
def totalCheck(l): #l - lsit

    if sum(l) == 120:
        return True
    else:
        print("\nTotal Error: Please enter the correct volume of credits!")
        return False

def collectResults(): #p - passed, d - deferred, f - failed

    while True:
        
        try:
            p = int(input("\nPlease enter volume of credits at Pass level: "))
            d = int(input("Please enter volume of credits at Defer level: "))
            f = int(input("Please enter volume of credits at Fail level: "))

            return [p,d,f]
        
        except ValueError:
            print("\nData Type Error: Please ensure that you insert a valid integer!")

def displayOutcomes(d): #l - dictionary

    t = 0

    print("\nStudent Progression Outcomes\n")

    for key, value in d.items(): #displays contents as touple
        print(f"{key}({value}): {value*'*'}")
        t += value

    print(f"\n{t} outcomes in total.")

def displayOutcomesExtension(d): #d - dictionary, l - list, sl - sorted list, c - count, i|j - indecies

    l = list(d.values()) 
    sl = sorted(l) 
    c = 0

    print("")

    for key, value in d.items():
        print(f"{key}({value})", end =" ")

    print("")

    for i in range(sl[-1]): #selecting largest value from sorted list
        for j in l:
            
            if j > i:
                print("    *    ", end="   ")
            else:
                print("         ", end="   ")
                
        print("")
                
    print(f"\n{sum(l)} outcomes in total.")           
        
def predefinedResults(c): #c - count

    l = (
        (120,0,0),
        (100,20,0),
        (100,0,20),
        (80,20,20),
        (60,40,20),
        (40,40,40),
        (20,40,60),
        (20,20,80),
        (20,0,100),
        (0,0,120)
    )
    
    return l[c]
        
main()





    
    
