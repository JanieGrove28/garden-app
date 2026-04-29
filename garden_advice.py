# Garden Advice App

print("Welcome to the Garden Advice App!")

month = input("Enter the month: ")

if month == "December" or month == "January" or month == "February":
    print("It is summer. Water your plants regularly.")
elif month == "March" or month == "April" or month == "May":
    print("It is autumn. Time to prune plants.")
elif month == "June" or month == "July" or month == "August":
    print("It is winter. Protect plants from frost.")
elif month == "September" or month == "October" or month == "November":
    print("It is spring. Great time for planting.")
else:
    print("Invalid month entered")

