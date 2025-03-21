x = "HELLOWORLD"[9]
print(x)

#integer
y = 123
print(y+2345)
#float data type
z = 3.1459
print(z)
#boolean
True
False
num = len(input("what is your name: "))
print(type(num))
#casting from one type to another
num = str(num)
print("Your name has " + num + " characters")

#rounding
r = round(8/3,2)
#floor function
o = 8//3
print(str(r) +" "+ str(o))
int(o)
#cant use count++, you can only use count+=1
print(o)
#f-string
print(f"The length of your name is {num} the division of 8 and 3 rounded to two decimal places is {r}!")

#TIP CALCULATOR

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill? "))
total = round((total_bill/people)*(tip_percentage/100+1),2)
final = "{:.2f}".format(total)
print(f"Each person should pay: ${final}")
