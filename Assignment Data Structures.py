#List
#Excercise
#Q1 Create list of 5 random numbers and print the list
l1 = [5,17,12,8,20]
print("List:",l1)
#Q2 Insert 3 new Values to the list and print the updated list
l1.extend([9,15,6])
print("Updated List:",l1)
#Q3 Try to use a for loop to print each element in the list
for Numbers in l1:
    print(Numbers)


#Dictionary
#Exercise
#Q1 Create a dictionary with key name,age, and address and values John,25, and NewYork respectively
Person = {'Name':'John','Age':'25','Address':'New York'}
print("Person Dictionary:",Person)

#Q2Add a new key value-pair to the dictionary created in Q1  with key phone and value 1234567890
Person.update({'Phone':'1234567890'})
print("Updated Dictionary:",Person)


#Set
#Exercise
#Q1 Create a set with values 1,2,3,4,and 5
Numbers = {1,2,3,4,5}
print("Set:",Numbers)
#Q2 Add the values 6 to the set created in Q1
Numbers.add(6)
print("Updated set after addition:",Numbers)
#Q3 Remove the value 3 from the set created in Q1
Numbers.remove(3)
print("Updated set after removal:",Numbers)


#Tuple
#Exercise
#Q1 Create a tuple with values 1,2,3,and 4
numbers = (1,2,3,4)
print("Tuple:",numbers)

#Q2 Print the length of tuple created in Q1
Length = len(numbers)
print("length of tuple:",Length)




