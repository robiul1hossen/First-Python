# escape sequence character
str = 'This is a string \nI am using escape sequence character here'
print(str)

# concatenation
str1='Hello'
str2='world'
finalStr = str1+" "+str2
print(finalStr)


# length
print(len(finalStr) )


# indexing      cannot change string using index finalStr[2]="B"
print(finalStr[6])


# Slicing       It do not print the last index
fullName = "mohammad Robiul Hossen"
print(fullName[9:16])
print(fullName[9:])
print(fullName[:9])

# endsWith
print(fullName.endswith('en'))
# startswith
print(fullName.startswith('M'))
# capitalize
print(fullName.capitalize())
# replace
print(fullName.replace('Hossen','Hasan'))
# find
print(fullName.find('h'))
# count
print(fullName.count('o'))


# practice problem -1 : print length of user name 
# name = input('Enter Your Name: ')
# print(len(name))

# practice problem -2 : print the count of $ symbol in string
# string = input('Enter Your String Here: ')
# print(string.count('$'))


# conditions
age = 14
if(age>=18):
    print("can vote")
else:
    print('cannot vote')

marks = float(input('Enter Your Marks To Calculate Your Grade: '))
if(marks < 0 or marks > 100):
    print('Please Provide A Valid Number')
elif(marks>=90 and marks<=100) :
    print('Your Grad Is A+')
elif(marks>=80 and marks<90) :
    print('Your Grad Is A')
elif(marks>=70 and marks<80) :
    print('Your Grad Is A-')
elif(marks>=60 and marks<70) :
    print('Your Grad Is B')
elif(marks>=50 and marks<60) :
    print('Your Grad Is C')
elif(marks>=40 and marks<50) :
    print('Your Grad Is D')
elif(marks>=30 and marks<40) :
    print('Your Grad Is E')
else:
    print('Sorry! You Are Fail')



# practice problem -3 : check a number is odd or even
number = int(input('Enter a number : '))

if(number % 2 == 0) : print('Even')
else : print('Odd')


# practice problem -4 : check the largest number 
num1 = 50
num2 = 60
num3 = 7
num4 = 100

if(num1 > num2 and num1 > num3 and num1 > num4):
    print('largest number is', num1)
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print('largest number is', num2)
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print('largest number is', num3)
else:
    print('largest number is', num4)


# practice problem -5 : check a number is divisible by 7 or not 

userNum1 = int(input('Enter a number : '))
print(userNum1)
if(userNum1 % 7 == 0):
    print('The number', userNum1, 'is divisible by 7')
else: 
    print('The number', userNum1, 'is not divisible by 7')