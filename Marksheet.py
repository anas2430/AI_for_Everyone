english = int(input("Enter English Marks :"))
Maths = int(input("Enter Maths Marks :"))
Chemistry = int(input("Enter Chemistry Marks :"))
Physic = int(input("Enter Physic Marks :"))
Urdu = int(input("Enter Urdu Marks :"))
total_marks = (int(500))

percentage = int(english) + int(Maths) + int(Chemistry) + int(Physic) + int(Urdu)
total_sum = int(percentage)
final_percentage = total_sum / total_marks * 100
print("********************************")
print("Your Percentage is :", float(final_percentage))
print("********************************")

if final_percentage <= 39:
  print("You are Failed, Grade F")
  print("========================")

elif final_percentage <= 49:
  print("Your Grade is D")

elif final_percentage <= 59:
   print("Your Grade is C")

elif final_percentage <= 69:   
    print("Your Grade is B")

elif final_percentage <= 79:  
    print("Your Grade is A")     

elif final_percentage > 80:   
    print("Your Grade is A+")
    print("♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀♀")
else:
   print("Try Again....!")    