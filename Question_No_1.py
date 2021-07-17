#Write a function which takes a positive integer number n and
# prints [1 2 FIZZ 4 BUZZ FIZZ 7 8 FIZZ BUZZ 11 FIZZ 13 14 FIZZBUZZ … n]
# where multiples of 3 are replaced by FIZZ
# multiples of 5 are replaced by BUZZ
# multiples of both are replaced by FIZZBUZZ.

def bappyFizz(n):
    str1 = ''
    x = ''
    for i in range(1,n+1):
        if i%15 == 0:
            str1 += " FIZZBUZZ"
        elif i%3 == 0:
            str1 += " FIZZ"
        elif i%5 == 0:
            str1 += " BUZZ"
        else:
            x = str(i)
            str1 += " "+x
    print(str1)

def testcase():
    flag = 0
    f = open("testcase.txt", "r")
    for i in f:
        i = i.replace('\n','')
        if 'Question no.1' in i:
            flag = 1
        if 'Question no.2' in i:
            flag = 0        
        if flag == 1 and not 'Question no.1' in i:
            print("\nInput number: "+i)
            bappyFizz(int(i))

print('1.Default Testcases\n2.Custom input')
choice = int(input())
if choice == 1:
    testcase()
elif choice == 2:
    print("Enter an input string:")
    bappyFizz(int(input()))
else :
    print("Invalid")