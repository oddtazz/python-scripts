#!/usr/bin/python

selection = raw_input("Enter \n\
1 to convert int to binary\n\
2 to convert binary to int\n\n")

if selection == "1":
  number = raw_input("Enter the number to convert : ")
  number = int(number)
  bin = bin(number)
  print bin
elif selection == "2":
  number = raw_input("Enter the binary number : ")
  print int(number, 2)
else :
  print "You didnt type 1 or 2 buddy. Try again."
