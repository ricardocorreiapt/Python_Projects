print("How much years to get 1 million -.- :) ")
#get the age
age = int(input("How old are you? :"))
##calculate moth income
salary=int(input("How much you make per moth? :"))
#makes the income * 12 moths(1 year)
peryear = salary * 12
# calculate the years to get 1 million
million =  1000000 // peryear
#Show the years that will take
print ("It Will take ", million , "years") 
#Add the million years to the age and show it 
result = million + age
print("You will get 1 million by the Age of ",result)






