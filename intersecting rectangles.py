def luna():
    x = input ("Give me the coordinates of the two rectangles. ")#input would be like '[0,0, (width),(length)]*2
    list = x.split('][')
    rectangle1,rectangle2 = list[0],list[1]
    rectangle1=rectangle1.split(',')
    rectangle2=rectangle2.split(',')
    area1 = []
    area2 = []
    for i in range(1,int(rectangle1[2])+1):
        minilist = [int(rectangle1[0])+i,int(rectangle1[1])]
        area1.append(minilist)
    for i in range(1,int(rectangle1[3])):
        minilist = [int(rectangle1[0]),int(rectangle1[1])+i]
        area1.append(minilist)

    for i in range(1, int(rectangle2[2]) + 1):
        minilist = [int(rectangle2[0]) + i, int(rectangle2[1])]
        area2.append(minilist)
    for i in range(1, int(rectangle2[3]) + 1):
        minilist = [int(rectangle2[0]), int(rectangle2[1]) + i]
        area2.append(minilist)
    print ('area1', area1)
    print ('area2', area2)
    for i in area1:
        print ('i:',i)
        if i in area2:
            return True
    return False

from graphics import *
def find_int (R1, R2):

    win = GraphWin('Rect', 400, 400) # give title and dimensions
    #win.yUp() # make right side up coordinates!

    head1 = Rectangle(Point(R1[0], R1[1]), Point(R1[0] + R1[2], R1[1] + R1[3]))
    head1.setFill("red")
    head1.draw(win)

    head2 = Rectangle(Point(R2[0], R2[1]), Point(R2[0] + R2[2], R2[1] + R2[3]))
    head2.setFill("blue")
    head2.draw(win)
    #label = Text(
    #label = Text(Point(100, 120), 'A face')Point(100, 120), 'A face')
    #label.draw(win)

    #figure out overlap here
    ret = True
    if R2[1] >= R1[1]+R1[3]:
        ret = False
    elif R1[1] >= R2[1]+R2[3]:
        ret = False
    elif R2[0] >= R1[0]+R1[2]:
        ret = False
    elif R1[0] >= R2[0]+R2[2]:
        ret = False
    else:
        ret = True
        listx = [R1[0],R1[0]+R1[2],R2[0],R2[0]+R2[2]]
        listx.sort()
        listy = [R1[1],R1[1]+R1[3],R2[1],R2[1]+R2[3]]
        listy.sort()
        intersection = Rectangle(Point(listx[1],listy[1]),Point(listx[2],listy[2]))
        intersection.setFill("yellow")
        intersection.draw(win)
    label = Text(Point(100, 120), ret)
    label.draw(win)
    win.getMouse()
    win.close()
    return ret

def random_numbers():
    list = []
    import random
    for i in range(4):
        x = random.randint(0,400)
        list.append(x)
    return list

def calling_main():
    for i in range(10):
        x = random_numbers()
        y = random_numbers()

        z = find_int(x, y)
        print (x,y,z)



calling_main()