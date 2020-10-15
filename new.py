def Income(hours,per_hour):
    Total_income = hours * per_hour
    return Total_income
hours = input('please enter hours')
hour = int(hours)
print(Income(hour , 20000))