print("hello world")
age=20
print(age)
age=10 #overriding variable value
print(age)

#-----user input prompt-------#
name = input("What is your name?: ")
print("Hello "+ name)

#-----Type casting-------#
year = input("what is your birthYear?: ") #input() returns a string type
age = 2024 - int(year) #type casting year from string to int
print("Your Age is: ", age)

#-------Concatination-------#
#Only strings can be concatenated
first = input("Enter First value: ") 
second = input("Enter Second Value: ")
total = first + second 
print(total) # assuming first:1 and second:2, then it shows 12 as string concat. We need to type case
total = float(first) + float(second) #after type casting sum will work
print(total)

#------String methods-----#
course = "Python for Beginners"
print(course.upper())
print(course.lower())
print(course.find("y")) # returns position of first occurance of y i.e. 1
print(course.find("for")) #returns 7
print(course.replace("for","4"))
print('for' in course) #check if for exists in the var, it does

#-------Arithematic Operators------#

print(10 + 2)
print(10 -2)
print(10 * 2)
print(10 / 3) #3.33333
print(14 // 3) #returns only Quotiant 4
print(10 % 3) #returns only remainder
print(10 ** 3) #10^3 = 1000

#-----------If loop------#

temperature = 25
if (temperature < 30):
    print("It's a Pleasant weather")
elif(temperature > 30):
    print("It's hot!")
else:
    print("Temperature is 30 Degrees")
print("Have a nice day!")


#-----Convert weight to Lbs/KB--------#
unit = input("Enter unit (K for KB, L for LB): ")
weight = float(input("Enter weight: ")) #input returns string so we typecast it to float for calculations

if (unit == 'k' or unit == 'K'): 
    newweight = weight * 2.20462
    print("Your weight in Lbs is: ", newweight) #might need to type-cast string(newweight) but during our testing was not required
else:
    newweight = weight/2.20462
    print("Your weight in Kgs is: ", newweight)

#------While loop-----#
i = 0
while(i < 5):
    print("This is line#", i)
    i+= 1

#-----print * --------#
i = 1
while(i < 5):
    print(i * "*") #we can multiply int and string, this means repeat the string i times
    i += 1

#-------Arrays------#
num = ['A','B','C','D']
print(num[0])
print(num[3])
print(num[-1]) #print last value of array
print(num[-2]) #print second last value of array

#-------Methods-------#
num = [10,20,30,40]
num.append(50) #add 50 to end of array
print(num)

num.remove(50) #remove value 50 in array, will throw error if 50 does not exist
print(num)
print(1 in num) #True is 1 exists else False
print(len(num))
num.clear() #empties the whole array
print(num)

#---For Loop-----#

number = [1,2,3,4,5]
for num in number: #here num is a temp variable we created
    print(num)

#----------WhileLoop-----------#
num = [1,2,3,4,5]
i = 0
while(i<5):
    print(num[i])
    i+= 1

#______Range() function____#
    
for num in range(5): #0-4
    print(num)
for num in range(5,10): #5-9
    print(num)
for num in range(5,10,2): #start from 5 take 2 steps : 5,7,9
    print(num)

#------Tuples------#
#Tuples means immutable i.e. cannot be changed
num_array = [1,2,3,4] #array
tuple_num = (1,2,3,4) #() means it's tuple i.e. cannot be changed
num_array[0] = 10
print(num_array)
tuple_num[0] = 10 #TypeError: 'tuple' object does not support item assignment
print(tuple_num)