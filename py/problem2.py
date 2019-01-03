# Panashe Katema --- Last Edited 03/01/2019

def Fibonacci(n): #Will generate the fibonnacci sequence up until the next term exceeds a specified value
    fib=[1,2]
    c=2 #counter
    f=fib[c-1]
    while f<n:
        f = fib[c-1] + fib[c-2] #next term in the seqeunce
        fib.append(f)
        c+=1
    return fib

def GetEvens(list): #Takes a list of ints and returns the even numbers
    evens=[]
    for x in list:
        if x%2==0:
            evens.append(x)
    return evens

print(sum(GetEvens(Fibonacci(4000000))))
