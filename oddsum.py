#This program will return the sum of all odd numbers within a range from a to b.
oddnumbers = []

def oddsum(a,b):
    for number in range(a,b+1):
        if number%2 == 1:
            oddnumbers.append(number)
    c=sum(oddnumbers)
    print(c)
