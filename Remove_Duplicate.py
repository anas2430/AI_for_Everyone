      
list1 = [1,2,3,4,1,2,3,4,6,8,9]
print("This is my list", str(list1))

result = []
for i in list1:
   if i not in result:
         result.append(i)
print("This is my list", result) 