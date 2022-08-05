#Student Version of the program (Part 1)

def main():

    try:
        passed = int(input("Please enter volume of credits at Pass level: "))
        deferred  = int(input("Please enter volume of credits at Defer level: "))
        failed = int(input("Please enter volume of credits at Fail level: "))

        #If within range!
        
        if passed == 120:
            print("Progress")
        elif passed == 100:
            print("Progress - module trailer")
        elif failed >= 80:
            print("Exclude")
        else:
            print("Do not progress - module retriever")
        
    except:
        print("Data Type Error: Please ensure that you insert a valid integer!")


main()

#combine or clean both functions
#can make a list and call for loop to run range check?

def rangeCheck(c):

    if c%20 == 0:
        return True #i += 1, if i = 3 (then all true)...
    else:
        return False

def rangeCheckAll(p, d, f):

    if p+d+f == 120:
        return True
    else:
        return False


    
    
