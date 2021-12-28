#user input of age

age = input("What is your current age?")

#figure out the days, weeks, months, years left using user input up to the age of 90

age_as_int = int(age)
years_left = 90 - age_as_int
weeks_left = years_left * 52
months_left = years_left * 12
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
