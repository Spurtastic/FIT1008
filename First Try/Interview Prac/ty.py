def factorial(n):
    if n == 0:
        return 1 
    else:
        return n*factorial(n-1)

print(factorial(5))




lst =[x for x in range(0,4)]
for i in range(0, len(lst)):
    print(lst[i])


