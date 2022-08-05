#Student Version of the program (Part 1)

def main():

    running = True

    while running:

        try:
            passed = int(input("Please enter volume of credits at Pass level: "))
            deferred  = int(input("Please enter volume of credits at Defer level: "))
            failed = int(input("Please enter volume of credits at Fail level: "))

            #If within range!

            if rangeCheck(passed, deferred, failed):
                
                if passed == 120:
                    print("Progression outcome: Progress")
                elif passed == 100:
                    print("Progression outcome: Progress - module trailer")
                elif failed >= 80:
                    print("Progression outcome: Exclude")
                else:
                    print("Progression outcome: Do not progress - module retriever")

                running = False
                    
            else:
                print("Range Error: Please enter vlues within the correct range!")
            
        except:
            print("Data Type Error: Please ensure that you insert a valid integer!")

#combine or clean both functions
#can make a list and call for loop to run range check? #seperate

def rangeCheck(p, d, f):

    l = [p,d,f]
    c = 0

    for i in l:
        if i%20 == 0:
            c += 1
        else:
            continue
    
    if sum(l) == 120 and c == 3:
        return True
    else:
        return False
        
main()





    
    
