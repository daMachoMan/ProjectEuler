# Panashe Katema --- Last Edited 05/02/2018

def Multiples(max,x): #Creates an array of the multiples of x up to the max value
    y=1
    maxNotReached = True
    multiList=[]
    while maxNotReached:
        a = x*y
        if a < max:
            multiList.append(a)
        else:
            maxNotReached = False
        y+=1
    return multiList
#--------------------------------------
def ArrayDiff(a1,a2): #Combines 2 arrays and removes duplicates.
    combinedList=a1
    for i in a2:
        if i not in a1:
            combinedList.append(i)
    return sorted(combinedList)
#--------------------------------------
n1=int(input("Find multiples of...  "))
n2=int(input("And... "))
maxNumber=int(input("Up to... "))

multiA = Multiples(maxNumber,n1)
multiB = Multiples(maxNumber,n2)

MultiAorB = ArrayDiff(multiA,multiB)

print(sum(MultiAorB))
