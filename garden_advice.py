def get_season(month):
    seasons = {
        "summer": ["December", "January", "February"],
        "autumn": ["March", "April", "May"],
        "winter": ["June", "July", "August"],
        "spring": ["September", "October", "November"]
    }

    for season, months in seasons.items():
        if month in months:
            if season == "summer":
                return "Summer - Water your plants regularly."
            elif season == "autumn":
                return "Autumn - Time to prune plants."
            elif season == "winter":
                return "Winter - Protect plants from frost."
            elif season == "spring":
                return "Spring - Great time for planting."

    return "Invalid month"


print("Welcome to the Garden Advice App!")
month = input("Enter the month: ")
print(get_season(month))