# Variables
name = "alexander coder"
age = 25
cohort = "2026-Alpha"
fav_topic = "Data Structures"
current_week = 3
total_weeks = 12

# Logic
formatted_name = name.title()
topic_display = fav_topic.replace(" ", "_")
weeks_left = total_weeks - current_week

# Output
print("-" * 30)
print(f"ID CARD: {formatted_name.upper()}")
print("-" * 30)
print(f"Age:      {age}")
print(f"Cohort:   {cohort}")
print(f"Topic:    #{topic_display}")
print(f"Week:     {current_week}")
print("-" * 30)
print(f"FOOTER: {weeks_left} weeks remaining in the program.")
print("-" * 30)