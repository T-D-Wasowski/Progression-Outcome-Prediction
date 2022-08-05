def main():

    print("Welcome to the progression outcome predictior!")

    outcomeCount = {
        "Progress": 0,
        "Trailer": 0,
        "Exclude": 0,
        "Retriever": 0
    }

    while True: #2
    
        while True: #1

            results = collectResults()

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

                break #1

            else:
                continue

        choice = input("\nPress 'Q' to display outcome results and quit, or any other key to continue: ").lower()
        

        if choice == "q":
            displayOutcomesExtension(outcomeCount)
            break #2
        else:
            continue
            
        

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

def displayOutcomesExtension(d): #d - dictionary, l - list, i - index

    l = list(d.values()) #dictionary values into list
    sl = sorted(l) #sorted list to get largest value for loop
    c = 0

    print("")

    for key, value in d.items():
        print(f"{key}({value})", end =" ")

    print("")

    for i in range(sl[-1]): #selecting largest value
        for j in l:
            
            if j > i:
                print("    *    ", end="   ")
            else:
                print("         ", end="   ")
                
        print("")
                
    print(f"\n{sum(l)} outcomes in total.")           
        
     
        
main()





    
    
