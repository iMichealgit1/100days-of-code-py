#DAY1 
print("Hello World!")
print("Day1-Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#New Line in python
print("Hello World!\nHello World!\nHello World!")

#Concatenation of strings
print("Hello" +" "+ "Micheal")
#" " means space

#avoid indentation error when coding in python i.e start each line of code from the beginning 

#Debugging exercise..fix the code below
print("Day1 -String Manipulaton") #it missed an opening quotation
print('String concatenation is done with the"+"sign.')# it missed the quotation marks for spacing
print('e.g. print("Hello World")')#indentation error
print("new lines are created with a back slash and n.") #it had 2 opening parenthesis

#User input- asking user for data input
# INPUT function is used here i.e input("a prompt for the user")
input("What is your name? ")
print("Hello "+input("what is your name? ")+"!")

# use ctrl +/ for turning highlighted words or code into COMMENT
# Exercise-Write a program that prints the number of characters in user name
print(len (input("Enter your name ") ) )
#or
name=input("What is your name?")
length =len(name)
print(length)

#len() is used to print length of a string
print(len("Adeolu"))

#python variable is a reserved memory location used to store data temporarily
name="Micheal"
print(name)

#Variable Exercise-Write a program that switches values stored in variable a and b
a=input("a:")
b=input("b:")
#Solution1; it's wrong
print("a:" + b)
print("b:" + a)
# Solution2: Right one
c=a
a=b
b=c
print("a:" + a)
print("b:" + b)

#variable naming-use underscore to separate words--also, numbers can't start a variable
#do not use reserved keywords

