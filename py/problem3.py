# Panashe Katema --- Last Edited 03/01/2019

def IsPrime(n): #Given a number this will tell you if its prime
    x=2
    halfn=n/2.0
    while x<halfn:
        if n%x==0:
            return False
        x+=1
    return True

def NextPrime(n): #Given a number this will return the next prime number
    n=n+1
    notFound=True
    while notFound:
        if IsPrime(n):
            notFound=False
        else:
            n+=1
    return n

def PrimeFactors(n): #Given a number, will return prime factors as a list
    x=2 #This is the prime number that will be checked
    a=n #This is the number that will decrease as prime factors are taken.
    primeFactors=[]
    found=False
    while found==False:
        if a%x==0:
            primeFactors.append(x)
            a=a/x
        elif a==1:
            found=True
        else:
            x=NextPrime(x)
    return primeFactors

test=int(input("Enter a number: "))
pfacts=PrimeFactors(test)
print("Here are the prime factors: ")
print(pfacts)
