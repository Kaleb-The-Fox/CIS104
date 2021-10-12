def maximum(a, b, c):

    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


a = 10
b = 2
c = 15
print(maximum(a, b, c))

a = 25
b = 90
c = 54
print(maximum(a, b, c))

a = 76
b = 23
c = 46
print(maximum(a, b, c))
