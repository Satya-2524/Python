
# print("hai")
# quetion1

num1=float(input("enter the number"))
if num1 > 0:
    print("positive number")
elif num1==0:
    print("zero")
else:
    print("negative number")

    
# quetion 2

num1=float(input("enter the number"))
if num1 %2==0:
    print("even")
else:
    print("odd")

#quetion 3
num2=float(input("enter the age: "))
if num2>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")
    
#gretest of two numbers
num3=float(input("enter the 1st number"))
num4=float(input("enter the 2nd number"))
if num3>=num4:
    print("gretest number")
else:
    print("lowest number")
    
# student marks
num5=float(input("enter the marks"))
if num5>40:
    print("student is pass")
else:
    print("student is fail")

#display the day
day=float(input("enter the number"))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("wensday")
elif day==4:
    print("Thurday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Not a day") 

#operators
operation=input("Enter the operation: ").lower()
num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))
if operation =='add':
    print(num1+num2)
elif operation =='sub':
    print(num1-num2)
elif operation == 'mul':
    print(num1*num2)
elif operation =='div':
    if num2==0:
        print("Divisible not possible")
    else:
        print(num1/num2)
else:
    print("it is not perform any operation")

# display a month
month=float(input("enter the month"))
if month==1:
    print("jan")
elif month==2:
    print("feb")
elif month==3:
    print("march")
elif month==4:
    print("april")
elif month==5:
    print("may")
elif month==6:
    print("jun")
elif month==7:
    print("july")
elif month==8:
    print("agust")
elif month==9:
    print("september")
elif month==10:
    print("october")
elif month==11:
    print("november")
elif month==12:
    print("december")
else:
    print("not a month")

# write a program to find a greatest of three numbers
a=float(input("Enter the first number:" ))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number: "))
if a>b and a>c:
    print(a," is greater number")
elif b>c:
    print(b,"is grater number")
else :
    print(c,"is greater")
   
 
#  write a program to classify a character  vowel or consonant

char=input("Enter character: ")
if char.isalpha():
    if char in('a','e','i','o','u'):
        print("vowel")
    else:
        print("consonant")
else:
       print("neither")
    
#  calculate the grade of a student
# 1.90-100 grade a
# 2.80-89 grade b
# 3.70-79 grade c
# 4.<70 

result=float(input("Enter the result"))
if result>=90 and result<=100:
    print("Grade A")
elif result>=80 and result<=89:
    print("Grade B")
elif result>=70 and result<=79:
    print("Grade c")
elif result>70:
    print("Fail")

# three side length from a valid triangle
s1=float(input("Enter the first number: "))
s2=float(input("Enter the second number: "))
s3=float(input("Enter the third number: "))
if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    print("valid Triangle")
else:
    ("Invalid Triangle")
    