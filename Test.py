
#========================= Q1 ==============================
# #Make Calculator")

# val1 = int(input("Enter any number : "))
# op = input ("enter the operator : ")
# val2 = int(input("Enter any number : "))


# if op == "+" :
#     print ("The sum of the number is ", val1 + val2 )

# if op == "-" :
#     print ("The sum of the number is ", val1 - val2 )

# if op == "*" :
#     print ("The sum of the number is ", val1 * val2 )

# if op == "/" :
#     print ("The sum of the number is ", val1 / val2 )

#========================= Q2 ==============================


#Create a Programme to print Even numbers.

# for x in range (0,10000,2):
#     print(x)



#========================= Q3 ==============================

#Create a Programme to print Odd numbers.

# for x in range (1,10000,2):
#     print(x)



#========================= Q4 ==============================

#Create a Programme to print Prime numbers.

# Val1 = int(input("Enter any number : "))

# if Val1 > 1 :
#     for x in range (2,Val1) :
#         if (Val1 % x) == 0 :
#             print("This is not a prime number ")
#             break
#         else :
#            print("This is a prime number")     
#            break


#========================= Q5 ==============================

#Create a Student Marksheet with user input Suject ENGLISH, MATHS, PHYCIS, CHEMISTRY, URDU and calculate
#Percentage and assign Grade according to their numbers.

# sub1 = int(input("Enter Marks in subject 1 : "))
# sub2 = int(input("Enter Marks in subject 2 : "))
# sub3 = int(input("Enter Marks in subject 3 : "))
# sub4 = int(input("Enter Marks in subject 4 : "))
# sub5 = int(input("Enter Marks in subject 5 : "))
# sub6 = int(input("Enter Marks in subject 6 : "))

# total_marks = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 
# percentage  = total_marks * 100 / 600

# print (percentage , "%")

# if percentage > 0 and percentage == 20 :
#     print ("Your Grade is F ")

# elif percentage > 20 and percentage == 40 :
#     print ("Your  Grade is C")

# elif percentage > 40 and percentage == 60 :
#     print ("Your Grade is B")

# elif percentage > 60 and percentage == 80 :
#     print ("Your Grade is A")

# elif percentage > 80 and percentage == 100 :
#     print ("Your Grade is A+")

#========================= Q6 ==============================


#Give user input and Print Table of it in Table format 1 to 10.

# val = int (input("Enter any number : "))

# for x in range (0,11):
#     print (val , "x" , x , "=" , val * x )


#========================= Q7 ==============================

#Print the second item of the list.

# thislist = ["apple", "banana", "cherry"]
# new  = thislist[1]
# print (new)

#========================= Q8 ==============================

#change the value of a specific item, refer to the index number.

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "orange"
# print (thislist)

#========================= Q9 ==============================

#Print List through a for loop

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print (x)

#========================= Q10 ==============================


#Determine a specified item is present in a list use the in keyword.
thislist = ["apple", "banana", "cherry"]

# if "banana" in thislist:
#     print(thislist)

#========================= Q11 ==============================
#determine how many items a list has.
thislist = ["apple", "banana", "cherry"]

# print(len(thislist))

#========================= Q12 ==============================
#add an item "Orange" to the end of the list.
thislist = ["apple", "banana", "cherry"]

# thislist.append ("Orange")
# print (thislist)

#========================= Q13 ==============================
#Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]

# thislist.insert(1, "Orange")
# print (thislist)

#========================= Q14 ==============================
#Remove the Specified Item form the list with the name.
thislist = ["apple", "banana", "cherry"]

# thislist.remove("apple")
# print (thislist)

#========================= Q15 ==============================
#Remove the Specified index from the list (or the last item if the index is not specified).
thislist = ["apple", "banana", "cherry"]

# thislist.pop()
# print(thislist)

#========================= Q16 ==============================
#Delete this list completely.
thislist = ["apple", "banana", "cherry"]

# del.thislist
# print (thislist)

#========================= Q17 ==============================

#Remove the Specified index from the list.
thislist = ["apple", "banana", "cherry"]

# thislist.pop(2)
# print (thislist)

#========================= Q18 ==============================
#Empty this list.
thislist = ["apple", "banana", "cherry"]

# thislist.clear()
# print (thislist)

#========================= Q19 ==============================
#Copy this list within the second variable and print both variable
thislist = ["apple", "banana", "cherry"]


# mylist = thislist.copy()
# print (mylist)


#========================= Q20 ==============================
#Copy this list without using copy method.
thislist = ["apple", "banana", "cherry"]

# mylist = list(thislist)
# print (mylist)



#Using constructor to create a List.

mylist = list(("Apple","Orange","Banana"))
print (mylist)


