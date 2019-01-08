# Panashe Katema --- Last Edited 07/01/2019
#---using code from problem3.py ---------
def IsPrime(n): #Given a number this will tell you if its prime
    x=2
    while x<n:
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
#----------------------------------------
def SmallestMultiples(n): #Will find that smallest number divisible by 1->n
    factors=[]
    for i in range(2,n):
        if IsPrime(i):
            factors.append(i)
        else:
            a=PrimeFactors(i)
            for x in a:
                if (a.count(x))>(factors.count(x)): #Count is useful bank this one!
                    factors.append(x)
    return factors

test=int(input("Enter a number: "))
multis=SmallestMultiples(test)
total=1
for x in multis:
    total*=x
print(total)
