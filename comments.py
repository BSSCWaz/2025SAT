# The following details containt 2 examples of Internal Documentation (or commenting) in 
# relation to the inclusion of code you may may have copied from other resources, but 
# have included in your program. The two exmaples are referred to as Example 1 and Example 2.

# 
# ########################### Example 1 ###############################
#

# === begin copied resource ===
# The following code was taken from
# https://www.w3schools.com/python/python_dsa_bubblesort.asp on 13 Jun 2025
# and has been used to assist with blah blah blah

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)

# === end copied resource ===


# 
# ########################### Example 2 ###############################
#

# === begin copied resource ===
# The following code was taken from
# https://www.w3schools.com/python/python_dsa_bubblesort.asp on 13 Jun 2025
# and has been used to assist with blah blah blah

#mylist = [64, 34, 25, 12, 22, 11, 90, 5]

#n = len(mylist)
#for i in range(n-1):
#  for j in range(n-i-1):
#    if mylist[j] > mylist[j+1]:
#      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

# print(mylist)

# === end copied resource ===

# === begin modified resource ===
# I understand 
#  1) that mylist is a Python list,
#  2) that n will be an integer giving the length of mylist,
#  3) that the for loop will loop through the contents of the loop somehow,
#  4) that the if statement checks whether one value is greater than the other, and that
#  5) the print statement will print the list

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)

# === end modified resource ===
