x = eval(input("How many layers do you want? "))
def luna(n):
    list = []
    if n == 0:
        return list
    if n == 1:
        list = [[1]]
        return list
    for i in range(1,n+1):
        minilist = [1 for i in range(i)]
        list.append(minilist)
    for i in range(0,n):
        if i > 1:
            for j in range(1,i):
                list[i][j] = list[i-1][j-1] + list[i-1][j]
    return list

for i in luna(x):
    print (i)