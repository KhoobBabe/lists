def max_min(y):
    y.sort()
    print("The minimum number is ",y[0])
    y.reverse()
    print("The maximum number is ",y[0])
    
def sum_squ(y):
    squ = list(map(lambda i : int(i) * int(i), y))
    summ = 0
    for i in squ:
        summ += i
    print(summ)


def sort_asc(y):
    for i in range(len(y)):
        for j in range(i + 1, len(y)):

            if y[i] > y[j]:
                y[i], y[j] = y[j], y[i]
    print(y)




y = []
while y != "b":
    z = input("Enter a number or x to go to menu: ")
    if z != "x":
        if z.isdigit():
            y.append(int(z))
        else:
            print("Enter the numbers or x")
        
    elif z == "x":
        print("a.	Enter the list of numbers again")
        print("b.	Maximum and minimum numbers in the list ")
        print("c.	Sum of the squares of each number in the list")
        print("d.	Sort the list in ascending order ")
        print("e.	Exit the program")
        
        opt = input("select the option which you would like to do: ")
        if opt == "a":
            y = []
            z = input("Enter the value: ")
            if z != "x":
                if z.isdigit():
                    y.append(z)
                    
            else:
                print("Enter the numbers or X")
            
        elif opt == "b":
            max_min(y)
        elif opt == "c":
            sum_squ(y)
        elif opt == "d":
            sort_asc(y)
        elif opt == "e":
            print("program ended")
            break
