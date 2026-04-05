#Part A_List indexing (Question 1-8)
students=['Ali' , 'Sarah' ,'Hamza' ,'Zara' ,'Usman' ]
print(students[0])
print(students[-1])
print(students[2])
print(students[-4])
print(len(students))
print(students)
print(students[:3])
print(students[-2:])

#Part B_ Print Patterns (Question 9-12)
for i in range(1,6):
    print("* "*i)

for i in range(1, 6):
    print(' ' * (5 - i) + '*' *i)

for i in range(5, 0, -1):
    print(' * ' * i)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

#Part _B (if , else, elif statements )

age=int(input('Enter your age :'))
if age>=18:
    print('You are Adult')

else :
    print('YOU ARE YOUNGER')

Student_Marks=int(input('Enter student marks:'))

if Student_Marks>=50:
    print('You are PASS!')
    print('CONGRATULATIONS!')
else:
    print('YOU ARE FAIL!')
    print('GOOD LUCK FOR NEXT TIME')

#grades calculator
marks=int(input('ENTER MARKS:'))
if marks >=90:
    print('GRADE = A+')
    print('REMARKS = Outstanding!')
elif marks >=80:
    print('GRADE = A')
    print('REMARKS = Excellent!')
elif marks >=70:
    print('GRADE = B')
    print('REMARKS = Good')
elif marks >=60:
    print(' GRADE = C')
    print('REMARKS = Satisfactory!')
elif marks >=50:
    print(' GRADE = D')
    print('REMARKS = Need improvement!')
else:
    print('Fail')
    print('REMARKS = Better next time')

#ATM Withdrowar
amount=10000
pin=1234
pin=int(input('Enter the pin :'))
if pin==1234:
    amount_Required=int(input('ENTER THE AMOUNT:'))
    if amount_Required >=amount:
        print('Unsufficient fund!')
    else:
        amount-=amount_Required
        print('Remaining amount=' , amount )
else:
    print('Wrong pin!')

#task 5
#If-else is used for 2 possible outcomes, while if-else-elif is used for multiple outcomes.
#If-else checks a single condition, whereas if-else-elif checks multiple conditions.
#A nested if statement is used to check another condition inside an existing if statement, allowing multiple conditions to be evaluated.
#- If-else: Age is above 18, you can vote, otherwise you can't.
#- If-else-elif: Marks are above 90, grade A. Marks are above 80, grade B. Otherwise, grade C.
#- Nested if: If you're a student, if your marks are above 80, you're eligible for scholarship.