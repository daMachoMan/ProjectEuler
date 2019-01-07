# Panashe Katema --- Last Edited 07/01/2019

def IsPalindrome(n):
    if (str(n)[::-1])==str(n):
        x=True
    else:
        x=False
    return x

def PalindromeFinder(n): #Where n is number of digits for the factors
    max=(10**n)
    min=10**(n-1)
    PalNFactors=[1,1,1]
    for x in range(min,max):
        for y in range(min,max):
            a=x*y
            if IsPalindrome(a):
                if a > PalNFactors[0]:
                    new=[a,x,y]
                    PalNFactors=new
    return PalNFactors

test=int(input("Enter digits: "))
print(sorted(PalindromeFinder(test)))
