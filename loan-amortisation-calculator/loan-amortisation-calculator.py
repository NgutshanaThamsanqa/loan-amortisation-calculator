import math
import pandas as pd
import numpy as np

#Get loan amount and number of years
def get_user_input():
    loan_amount =  float(input("Enter your loan amount R: "))
    deposit = float(input("Enter deposit amount R: "))
    loan_term = int(input("Enter loan term (in years): "),0)           
    
    loan_inclusive_deposit = loan_amount - deposit
    
    amortisation_variables.update({"loan amount":round(loan_inclusive_deposit, 2), "number of years":loan_term})
    
    #Perform Services
    service_the_user() #Perfom user request

#Calcalate montly interest rate (Option 1)
def monthly_interest_rate ():
    monthly_interest = amortisation_variables["interest"]/12
    return round(monthly_interest,2)

#Calculate number of payment
def total_num_of_payment ():
    total_num_of_payment = amortisation_variables ["number of years"]*12
    return round(total_num_of_payment)

#Calculate monthly payment using loan amortisation (Option 2)
def monthly_payment ():
    numerator = amortisation_variables["loan amount"] * monthly_interest_rate()
    denominator = 1 - pow(1 + monthly_interest_rate(), - total_num_of_payment())
    return round(numerator/denominator, 2)

#Generate loan schedule for user specified months (Option 3)
def generate_loan_schedule ():
    remaining_amount = amortisation_variables ["loan amount"]
    
    schedule = [] #schedule will store list of rows of loan amortisation schedule
    
    #Validate entered schedule months
    num_of_payment = total_num_of_payment ()
    scheduled_months = int(input("Enter loan schedule (in months): ")) #get the number of month
    
    while not (scheduled_months <=num_of_payment):
        print("Your number of months is not valid")
        scheduled_months = int(input("Enter loan schedule (in months): "))
    else: 
        for month in range (1,scheduled_months+1):
            interest_payment = remaining_amount *monthly_interest_rate()
            principal_payment = monthly_payment() - interest_payment
        
            remaining_amount -= principal_payment
        
            schedule.append({"Month": month, 
                         "Payment": f"R{monthly_payment()}",
                         "Interest Paid": f"R{round(interest_payment,2)}",
                         "Principal Paid": f"{round(principal_payment,2)}",
                         "Remaining Balance": f"R{max(0,round(remaining_amount, 2))}"}) #avoid negative remaining balance
     
        print(f"\n********************Payments for {scheduled_months} Months and Balances************************\n")
     
        df_schedule = pd.DataFrame(schedule)
        return df_schedule.to_string(index=False) #removes automatic 0-index


def service_option ():
    print('''\n"***************Welcome to the Loan Calculator***************
      Service Menu:
      1. Monthly payment
      2. Monthly interest rate
      3. Loan schedule
      ''')
    
    user_option = input("Enter a service number: ")
    
    #Validate Service Option
    while not (user_option == "1" or user_option == "2" or user_option == "3"):
        print("Your service option do not exist")
        user_option = input("Enter a service number: ")
    else: 
        return user_option
        
    

#Call Service Menu
def service_menu ():
    
    menu_options = {"1": monthly_payment,
                    "2": monthly_interest_rate, 
                    "3": generate_loan_schedule}
    
    return menu_options

#Perfom user request
def service_the_user():
    user_choice = service_option()
    action = service_menu().get(user_choice,"1")
    result = action()
    print(result)
    
    #Back to the Service Menu
    print('''\nService Menu:
      1. Service Menu
      2. Enter loan details
      3. Exit
      ''')
    
    user_option = input("Enter a service number: ")
    
    #Validate and Perfome user service
    while not (user_option == "1" or user_option == "2" or user_option == "3"):
        print("Your service option do not exist")
        user_option = input("Enter a service number: ")
    else:
        if user_option == "1":
            service_the_user()
        elif user_option == "2":
            get_user_input()
        else:
            print("Thank you for using our services")

                                          #Main  
#Get input
amortisation_variables = {"interest": 0.1025} #constant
get_user_input()







