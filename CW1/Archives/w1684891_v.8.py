def main():
    progressPrediction()

def staffExtention():
    pass

def progressPrediction():

    while True:

        volumes = collectInput()

        if rangeCheck(volumes) and totalCheck(volumes):
            
            if volumes[0] == 120:
                print("Progression outcome: Progress")
                
            elif volumes[0] == 100:
                print("Progression outcome: Progress - module trailer")
                
            elif volumes[2] >= 80:
                print("Progression outcome: Exclude")
                
            else:
                print("Progression outcome: Do not progress - module retriever")

            break

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

def collectInput(): #p - passed, d - deferred, f - failed

    while True:
        
        try:
            p = int(input("Please enter volume of credits at Pass level: "))
            d = int(input("Please enter volume of credits at Defer level: "))
            f = int(input("Please enter volume of credits at Fail level: "))

            return [p,d,f]
        
        except ValueError:
            print("Data Type Error: Please ensure that you insert a valid integer!")

main()





    
    
