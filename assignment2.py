your_name = input("enter your name: ")
reverse = your_name[::-1]
print("the reverse of your name is " + reverse)


Principal = int(input("Enter your principal amount: "))

Rate = int(input("Enter your bank rate: "))

num_year = int(input("Enter the number of years: "))

Compound_interest = Principal * (1 + Rate/100)**num_year

print("Your compound interest is " , Compound_interest)


Sentence = input("Write any senetnce of your choice: ")
first_letter = Sentence[0]
last_letter = Sentence[-1]
print("the first letter of your sentence is " + first_letter + " and the last letter of your sentence is " + last_letter)


Pounds = int(input("write an amount in pounds: "))
Conversion_from_pounds_to_naira = Pounds * 1951.15
print(Conversion_from_pounds_to_naira) 


Radius = int(input("Enter your given radius: "))
pie = 3.142
Circumference = 2 * pie * Radius
print("the circumference of your circle is " , Circumference)