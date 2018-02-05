# Panashe Katema --- Last Edited 05/02/2018

#Produces an array of multiplesOfFive
n = 1
multiples = []
while n*5<=1000:
    multiples.append(n*5)
    n  = n +1

#produces an array of multiples of three
m = 1
while m*3<=1000:
    if (m*3)/5 != 0:
        multiples.append(m*3)
    m = m+1
print(multiples.sorted())

print(sum(multiples))
