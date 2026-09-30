#simple calculations

current_year= int(input("Enter the current year: "))
birth_year= int(input("Enter your birth year: "))

#Calculate approximate age and age in 5 years and double your age

approximate_age= current_year - birth_year
age_in_five_years = approximate_age + 5
double_age = approximate_age * 2

print()
print("Age Calculations")
print("---------")
print(f"Approximate age is {approximate_age} and in 5 years will be {age_in_five_years} and double is {double_age}")