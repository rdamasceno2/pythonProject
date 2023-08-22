total_income = float(input("What is your annual income?"))
Employee_pension_contributions = float(input("What is your Pension contribution percentage?")) / 100

total_pension = total_income * Employee_pension_contributions
total_pension_monthly = total_pension / 12


def calculate_income_tax(income, pension=0.0):
    total_salary_sacrifice_income = income - pension
    if total_salary_sacrifice_income <= 12570:
        return 0
    elif 12571 <= total_salary_sacrifice_income <= 50270:
        return (total_salary_sacrifice_income - 12570) * 0.20
    elif 50271 <= total_salary_sacrifice_income <= 125140:
        return (total_salary_sacrifice_income - 50270) * 0.40
    else:
        return (total_salary_sacrifice_income - 125140) * 0.45


def calculate_national_insurance(income, pension=0.0):
    total_salary_sacrifice_income = income - pension
    if total_salary_sacrifice_income <= 12570:
        return 0
    elif total_salary_sacrifice_income <= 50270:
        basic_rate = (total_salary_sacrifice_income - 12570) * 0.12
        return basic_rate
    else:
        basic_rate = (50270 - 12570) * 0.12
        higher_rate = (income - 50270) * 0.02
        return basic_rate + higher_rate


national_insurance = calculate_national_insurance(total_income, total_pension)
national_insurance_monthly = calculate_national_insurance(total_income, total_pension) / 12
tax = calculate_income_tax(total_income, total_pension)
tax_monthly = calculate_income_tax(total_income, total_pension) / 12
taxable_wage = (total_income - 12570) - total_pension

net_income = 12570 + (taxable_wage - (tax + national_insurance))
net_income_monthly = net_income / 12


result_string = (
    f"Total Taxable Income at £{total_income:.2f} is £{taxable_wage:.2f}\n"
    f"Total tax applicable at £{total_income:.2f} is £{tax:.2f} annual or £{tax_monthly:.2f} monthly\n"
    f"National Insurance contribution at £{total_income:.2f} is £{national_insurance:.2f} annual "
    f"or £{national_insurance_monthly:.2f} monthly\n"
    f"Total Pension Contribution of £{total_income:.2f} at {Employee_pension_contributions:.2%} is £{total_pension:.2f} "
    f"annual or £{total_pension_monthly:.2f} monthly\n"
    f"Take Home Pay at £{total_income:.2f} is £{net_income:.2f} annual or £{net_income_monthly:.2f} monthly\n"
    "Disclaimer: Numbers may vary based on Tax Code or if you have any benefits in kind from the employer"
)

print(result_string)
