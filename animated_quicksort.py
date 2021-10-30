""" File:animated_quicksort.py
    Author:Xin Li
    Purpose:Animated QuickSort
"""
from graphics import graphics
import random

def runQuickSort(array):
    """This function calls quickSort function and print debug message
       Arguments: array is a list of integers
       Return Value: res is a list of integers
    """
    print("INPUT DATA: ",end="")
    printList(array)

    res=quicksort(array)
    print("AFTER THE SORT: ",end="")
    printList(res)
    return res

def runQuickSort2(array,p,time):
    """This function calls quickSort function
        and print debug message and animation
       Arguments: array is a list of integers, p is graphics,
        time is integer
       Return Value: res is a list of integers
    """
    print("INPUT DATA: ",end="")
    printList(array)
    box(array,100,100,p,50)
    res=quicksort2(array,p,time)
    print("AFTER THE SORT: ",end="")
    printList(res)
    return res

def box(array,x,y,p,size):
    """This function draws boxes
       Arguments: array is a list of integers, p is graphics,
        x, y, size are integers
       Return Value: no return value
    """
    if(len(array)==0):
        i=0
        p.rectangle(x+size*i,y,size,size,fill='black')
        p.rectangle(x+size*i+5,y+5,size-10,size-10,fill='white')
        return
    for i in range(0,len(array)):
        p.rectangle(x+size*i,y,size,size,fill='black')
        p.rectangle(x+size*i+5,y+5,size-10,size-10,fill='white')
        p.text(x+size*i+5,y+5,array[i])


def box2(array,x,y,p,size):
    """This function draws boxes
       Arguments: array is a list of integers, p is graphics,
        x, y, size are integers
       Return Value: no return value
    """
    for i in range(0,len(array)):
        p.rectangle(x+size*i,y,size,size,fill='black')
        p.rectangle(x+size*i+5,y+5,size-10,size-10,fill='pink')
        p.text(x+size*i+5,y+5,array[i])

def quicksort(array):
    """This function is the main quickSort funciton,
        including debug message printing
       Arguments: array is a list of integers
       Return Value: res is a list of integers
    """
    # Debug message
    if(len(array)==0 or len(array)==1):
        print("QS: The length of the input data, ",end="")
        print(array,end="")
        print(", is zero or one.  Returning immediately.")
        return array
    # pivot
    pivot=array[0]
    left=[]
    right=[]
    # Build left and right array
    for i in range(1,len(array)):
        if(array[i]<=pivot):
            left.append(array[i])
        else:
            right.append(array[i])
    # debug message
    print("QS: Data in: ",end="")
    printList(array)
    print("    Pivot:  ",pivot)
    print("    Left:    ",end="")
    printList(left)
    print("    Right:   ",end="")
    printList(right)
    # recursive call
    sortedLeft=quicksort(left)
    sortedRight=quicksort(right)
    # debug message
    print("QS: AFTER RECURSION...")
    print("    Original data:  ",end="")
    printList(array)
    print("    Left (sorted):  ",end="")
    print(sortedLeft)
    print("    Right (sorted): ",end="")
    print(sortedRight)
    print("    Sorted data:    ",end="")
    sortedLeft.append(pivot)
    # after recursive call
    res=sortedLeft+sortedRight
    printList(res)
    return res

def quicksort2(array,p,time):
    """This function is the main quickSort funciton,
        including debug message printing and animation function call
        and animation
       Arguments: array is a list of integers, p is graphics,
        time is integer
       Return Value: res is a list of integers
    """
    # Debug message
    if(len(array)==0 or len(array)==1):
        print("QS: The length of the input data, ",end="")
        print(array,end="")
        print(", is zero or one.  Returning immediately.")
        return array
    box(array,100,100,p,50)
    # pivot
    pivot=array[0]
    left=[]
    right=[]
    # Build left and right array
    for i in range(1,len(array)):
        if(array[i]<=pivot):
            left.append(array[i])
        else:
            right.append(array[i])
    pivotArray=[]
    pivotArray.append(pivot)
    # animation
    box(left,100,200,p,50)
    box(right,100+50*(len(left)+2)+150,200,p,50)
    box2(pivotArray,100+50*(len(left)+2)+50,200,p,50)
    # debug message
    print("QS: Data in: ",end="")
    printList(array)
    print("    Pivot:  ",pivot)
    print("    Left:    ",end="")
    printList(left)
    print("    Right:   ",end="")
    printList(right)
    # recursive call
    sortedLeft=quicksort2(left,p,time)
    sortedRight=quicksort2(right,p,time)
    # animation
    box(sortedLeft,100,300,p,50)
    box(sortedRight,100+50*(len(left)+1)+150,300,p,50)
    box2(pivotArray,100+50*(len(left)+1)+50,300,p,50)
    # debug message
    print("QS: AFTER RECURSION...")
    print("    Original data:  ",end="")
    printList(array)
    print("    Left (sorted):  ",end="")
    print(sortedLeft)
    print("    Right (sorted): ",end="")
    print(sortedRight)
    print("    Sorted data:    ",end="")
    sortedLeft.append(pivot)
    # after recursive call
    res=sortedLeft+sortedRight
    printList(res)
    # animation
    box(res,100,400,p,50)
    p.update_frame(time)
    p.clear()
    return res

def printList(list):
    """This function prints list
       Arguments: list is a list of integers
       Return Value: no return value
    """
    print("[",end="")
    for i in range(0,len(list)):
        if(i is not 0):
            print(", ",end="")
            print(list[i],end="")
        else:
            print(list[i],end="")
    print("]")

def random1(num):
    """This function build random list
       Arguments: num is a integer
       Return Value: res is a list of integers
    """
    res=[]
    count=0
    if(num==-1):
        count=20
    else:
        count=num
    for i in range(0,count):
        res.append(random.randint(-50,100))
    return res


def main():
    # Handle Input
    array=[]
    print("Frames per second?  (Give 0 to disable animation.)")
    frame=(float)(input())
    print("Please give the input data:")
    counter=0
    while True:
        try:
            line=input()
            # blank line, skip
            if(line==""):
                continue
            temp=line.split()
            for i in range(0,len(temp)):
                if(i==0 and counter==0 and temp[0]=="random"):
                    if(len(temp)==2):
                        array=random1((int)(temp[1]))
                    else:
                        array=random1(-1)
                    break
                else:
                    array.append((int)(temp[i]))
            counter=counter+1
        except EOFError as e:
            break
    if(frame==0):
        a=runQuickSort(array)
    else:
        # Main carvent
        p=graphics(1500,1000,"short")
        a=runQuickSort2(array,p,frame)
        # Hold the carvet
        p.mainloop()

main()
