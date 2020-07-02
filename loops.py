#Print i as long as i is less than 6:

i = 1
# while i < 6:
#   print(i)
#   i += 1

#The break Statement

#With the break statement we can stop the loop even if the while condition is true:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Print each fruit in a fruit list:
#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
 #
  for x in "banana":
      print(x)
#
#Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#
for x in range(6):
  print(x)

#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")