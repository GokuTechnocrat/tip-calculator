#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

total_bill=input("Enter the total bill amount\n")
# print(total_bill)

tip=input("Enter the amount you wanted to tip ,Make sure you enter the value in percentage\n")
# print(tip)


total_people=input("Enter the total no of people\n")
# print(type(total_bill))
# print(type(tip))


tot_bill=int(total_bill)
final_tip=int(tip)
tot_people=int(total_people)
tip_percent=(final_tip/100)*tot_bill
# print(int(tip_percent))
final_amt=int(total_bill)+int(tip_percent)
# print(int(final_amt))
Each_person_pay=int(final_amt)/int(total_people)
print(round(Each_person_pay))
print(f"Each person should pay,{Each_person_pay} rupees as their bill!")