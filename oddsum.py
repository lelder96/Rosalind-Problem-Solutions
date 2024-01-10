oddnumbers = []

def oddsum(a,b):
    for number in range(a,b+1):
        if number%2 == 1:
            oddnumbers.append(number)
    c=sum(oddnumbers)
    print(c)


oddsum(4435, 8480)



