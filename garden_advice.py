def get_season(month):
    """
    Returns gardening advice based on the given month.
    """

    seasons = {
        "summer": {"months": ["December", "January", "February"],
                   "advice": "Summer - Water your plants regularly."},

        "autumn": {"months": ["March", "April", "May"],
                   "advice": "Autumn - Time to prune plants."},

        "winter": {"months": ["June", "July", "August"],
                   "advice": "Winter - Protect plants from frost."},

        "spring": {"months": ["September", "October", "November"],
                   "advice": "Spring - Great time for planting."}
    }

    for season_data in seasons.values():
        if month in season_data["months"]:
            return season_data["advice"]

    return "Invalid month entered. Please try again."


def main():
    print("🌱 Welcome to the Garden Advice App 🌱")
    month = input("Enter the month: ").strip().capitalize()
    print(get_season(month))


if __name__ == "__main__":
    main()
