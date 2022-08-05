#Student Version of the program (Part 1)

def main(): #call this student version | Main to ask which version

    running = True

    while running:

        try:
            passed, deferred, failed = collectInput()
            
            volumes = [passed, deferred, failed] #change name?

            #If within range!

            if rangeCheck(volumes) and totalCheck(volumes):
                
                if passed == 120:
                    print("Progression outcome: Progress")
                elif passed == 100:
                    print("Progression outcome: Progress - module trailer")
                elif failed >= 80:
                    print("Progression outcome: Exclude")
                else:
                    print("Progression outcome: Do not progress - module retriever")

                running = False
                    
            
        except:
            print("Data Type Error: Please ensure that you insert a valid integer!")

#combine or clean both functions
#can make a list and call for loop to run range check? #seperate

def rangeCheck(l):

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
        

def totalCheck(l):

    if sum(l) == 120:
        return True
    else:
        print("Total Error: Please enter the correct volume of credits!")
        return False

def collectInput(): #is this necessary? Do part 2 first

    p = int(input("Please enter volume of credits at Pass level: "))
    d  = int(input("Please enter volume of credits at Defer level: "))
    f = int(input("Please enter volume of credits at Fail level: "))

    return p, d, f

main()





    
    
