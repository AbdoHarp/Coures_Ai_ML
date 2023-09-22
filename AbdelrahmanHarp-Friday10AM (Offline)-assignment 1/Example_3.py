

# part 1  ************************************************************************************
# annual_salary = float(input("Type annual salary here : "))
# portion_saved = float(input("Type the portion you want to save (as a decimal)      : "))
# total_cost = float(input("Type the cost of your dream house here : "))
# monthly_salary = (annual_salary / 12.0)
#
# portion_down_payment = 0.25 * total_cost
#
# current_savings = 0
#
# returns = (current_savings * 0.4) / 12
#
# overall_savings = returns + (portion_saved * monthly_salary)
# months = 0
# # Want to exit the loop when there is enough savings for a down payment
# while current_savings < portion_down_payment:
#     current_savings += current_savings * (0.4 / 12)  # Monthly interest
#     current_savings += monthly_salary * portion_saved  # Monthly savings
#     months += 1
# print("It will take {} months to save!".format(months))


# part 2 *************************************************************************************
# current_saving = 0
#
# annual_salary = int(input("Enter your annual salary:"))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
# total_cost = int(input("Enter the cost of your dream home:"))
# semi_annual_raise = float(input("Enter the semi- annual raise, as a decimal:"))
# portion_down_payment = total_cost * 0.25
# print("Down payment of {}".format(portion_down_payment))
# months = 0
# while current_saving <= portion_down_payment:
#     if months % 6 != 1:
#         current_saving = current_saving * 0.04 / 12 + annual_salary / 12 * portion_saved + current_saving
#         months += 1
#     else:
#         annual_salary = annual_salary * (1 + semi_annual_raise)
#         current_saving = current_saving * 0.04 / 12 + annual_salary / 12 * portion_saved + current_saving
#         months += 1
#
# print(months)








# This is just an experiment to find the result of the code you can try ********************
# *************************************************************************************************************


# Enter your annual salary: 120000
# Enter the percent of your salary to save, as a decimal: .10
# Enter the cost of your dream home: 1000000
# Number of months: 183

# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))
#
# portion_down = (total_cost * .25)
# current_savings = 0
# monthly_salary = (annual_salary / 12)
# interest_rate = .04
#
# # goal is to loop up until I have enough for the down payment
#
#
# print(total_cost)
# print(annual_salary)
# print(portion_saved)
#
# print("The downpayment required for this house is", portion_down)
#
# # need to use +=, otherwise you would have to do current saving = current savings + 1
#
# months = 1
#
# while current_savings < portion_down:
#     current_savings += current_savings * (.04 / 12)  # monthly interest
#     current_savings += portion_saved  # monthly savings
#     months += months + 1
#
# print("It will take", months, "months to save the needed down payment of", portion_down)