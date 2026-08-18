from datetime import datetime

def get_zodiac(month, day):
    dates = [
        (1, 20, "Capricorn"),
        (2, 19, "Aquarius"),
        (3, 21, "Pisces"),
        (4, 20, "Aries"),
        (5, 21, "Taurus"),
        (6, 21, "Gemini"),
        (7, 23, "Cancer"),
        (8, 23, "Leo"),
        (9, 23, "Virgo"),
        (10, 23, "Libra"),
        (11, 22, "Scorpio"),
        (12, 22, "Sagittarius"),
    ]
    for i, (m, d, sign) in enumerate(dates):
        if month == m and day < d:
            return dates[i - 1][2] if i > 0 else "Capricorn"
        if month == m and day >= d:
            return sign
    return "Capricorn"

birthday = input("Enter your birthday (YYYY-MM-DD): ")
date = datetime.strptime(birthday, "%Y-%m-%d")
print(f"Your zodiac sign is {get_zodiac(date.month, date.day)}")
