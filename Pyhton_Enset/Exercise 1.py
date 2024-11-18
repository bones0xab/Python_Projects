def DL(x,n):
    sum = 0
    for i in range(n):
        sum += ((-1)**i*(x)**(2*i + 1))/(2*i + 1)
    return sum

result1 = DL(3,2)
result2 = DL(0.5,10)
print(result1)
print(result2)


#Complexity  O(n)
