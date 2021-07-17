#Write a function which takes a positive integer number n
# Fibonacci sequence [1 1 2 3 5 8 13 … ] upto n.

def fibo(n):
    str1 = [1,1]
    if n == 0:
        str1 = []
    if n == 1:
        str1 = [1]
    if n > 2:
        x = 1
        y = 1
        for i in range(2,n):
            a = x+y
            str1.append(a)
            x = y
            y = a
    return (str1)

def testcase():
    flag = 0
    f = open("testcase.txt", "r")
    for i in f:
        i = i.replace('\n','')
        if 'Question no.2' in i:
            flag = 1
        if 'Question no.3' in i:
            flag = 0        
        if flag == 1 and not 'Question no.2' in i:
            print("\nInput number: "+i)
            fibo(int(i))

def input():
    print('1.Default Testcases\n2.Custom input')
    choice = int(input())
    if choice == 1:
        testcase()
    elif choice == 2:
        print("Enter an input string:")
        fibo(int(input()))
    else :
        print("Invalid")