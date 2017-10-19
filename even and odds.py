def luna(n):
    for i in range(0,len(n)):
        if n[i] % 2 == 1:
            dog = n[i]
            n.pop(i)
            n.append(dog)
    return n

a = luna([1,2,3,4,5,6,7,8])
print (a)

