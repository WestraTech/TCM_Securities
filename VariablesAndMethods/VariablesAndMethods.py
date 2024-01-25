#Programmer: Gabe Westra
#Program: Variables & Methods
#Date: 1.11.2024

quote = "All is fair in love and war!"
print(quote)
print(quote.upper()) #Uppercase Method
print(quote.lower()) #Lowercase Method
print(quote.title()) #Titlecase Method
print(len(quote)) #Length on characters in our quote
 
name = "Gabe" #String
age = 15 #int
gpa = 4.9 #float

print(age)
print(int(gpa)) #Takes a float into an int

print("\nMy name is " + name + " and I am " + str(age) + "with a GPA of " + str(gpa) + ".") #Concatenate variables while casting Int to Str

print("\nMy name is" ,name, "and I am" ,age, "with a GPA of", str(gpa) + ".") #Concatenating using s Comma instead of a + while casting our gpa variable into a string to account for the s[acing before the period

print("")

age =+ 1 #Adds one to the variable Age
print(age)

print("")

age =+ 10 #Adds ten to the variable Age
print(age)

print("")

birthday = "1"
age += birthday #We can add two variables with the values as Int together
print(age)
