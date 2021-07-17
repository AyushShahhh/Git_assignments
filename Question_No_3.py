#Write a function which takes a string s as input and prints the frequencies of all the words in the string.
#  eg: quick fox lazy dog quick donkey fire fox 
#  returns {quick: 2, fox: 2, lazy: 1, dog: 1, donkey: 1, fire: 1}.
#  Use <space>  as the delimiter to identify what a word is.

from typing import Counter



def freq(inputString):
    bufferString = ''
    inputString = inputString.split(' ')
    inputString = sorted(inputString)
    result = []
    for i in inputString:
        if not i in bufferString:
            i = i.replace(' ','')
            bufferString += i
            x = i+': '+str(inputString.count(i))
            result.append(x)
    
    print(result)

def testcase():
    flag = 0
    f = open("testcase.txt", "r")
    for i in f:
        i = i.replace('\n','')
        if 'Question no.3' in i:
            flag = 1
        if flag == 1 and not 'Question no.3' in i:
            print("\nInput string: "+i)
            freq(i.lower())

print('1.Default Testcases\n2.Custom input')
choice = int(input())
if choice == 1:
    testcase()
elif choice == 2:
    print("Enter an input string:")
    freq(str(input()))
else:
    print("Invalid")