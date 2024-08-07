import os
import time
from enum import IntEnum

daily_good_habits_dictionary = {
    "get up early": "Start your day early, which enhances productivity",
    "brush teeth": "Maintains good hygiene",
    "drink a glass of water": "Stay hydrated",
    "limit smartphone use in the morning": "Avoid distractions",
    "morning stretching": "Improve flexibility and reduce stress",
    "clean your workspace": "Promote a tidy and focused work environment",
}

elite_habits_dictionary = {
    "eat vegetables": "Maintain a balanced and healthy diet",
    "supplementation": "Enhance your diet with essential nutrients",
    "exercise regularly": "Boost mental clarity and physical health",
    "cold shower": "Increase alertness and resilience",
    "networking with peers": "Improve communication and professional relationships",
    "learn advanced programming skills": "Continuous learning is key to growth",
    "practice gratitude daily": "Cultivate a positive mindset",
    "prepare meals in advance": "Save time and ensure healthy eating",
    "take care of personal grooming": "Maintain a professional appearance",
    "focus on a healthy diet": "Support long-term health and well-being",
    "practice forgiveness": "Maintain mental peace and emotional health",
}

legendary_habits_dictionary = {
    "review daily goals every morning": "Stay focused on your objectives",
    "plan the next day in the evening": "Set yourself up for success",
    "step out of your comfort zone": "Encourage personal and professional growth",
    "replace a bad habit with a good one": "Key to a fulfilling life",
    "plan to eliminate bad habits": "Take control of your actions",
    "reduce dopamine-driven distractions": "Stay productive and focused",
    "express gratitude for achievements": "Appreciate your journey and progress",
}

bad_habits = {
    "eat excessive sugar": "Affects health and energy levels",
    "overeating": "Leads to sluggishness",
    "mindless social media surfing": "Wastes time and reduces productivity",
    "complaining": "Creates a negative atmosphere",
    "not drinking enough water": "Leads to dehydration and fatigue",
    "rushing tasks": "Reduces quality of work",
}

destructive_habits = {
    "swearing": "Creates a negative impression",
    "excessive complaining": "Can damage professional relationships",
    "boasting about every achievement": "Can come across as arrogant",
}

import os
import time
from enum import IntEnum

def reading_numbered_keys(dictionary):
    for i, key in enumerate(dictionary.keys()):
        print(f' {i+1} --> {key}')

def create_file_name(type_of_habits, timestr, dir_path):
    part_of_path = type_of_habits + timestr + ".txt"
    file_full_path = os.path.join(dir_path, part_of_path)
    return file_full_path

def open_file_for_safe_habits(path, key):
    with open(path, 'a+', encoding="UTF-8") as file:
        file.write(key)
        file.write('\n')

def read_habits_in_file(path):
    with open(path, 'r', encoding="UTF-8") as file:
        if "Good" in path:
            print("\n", "GOOD Habits")
        else:
            print("\n", "BAD HABITS")
        print(file.read())

def read_habits_and_feedback_wrapper(read_habits_in_file):
    def read_habits_in_file_wrapped(path):
        read_habits_in_file(path)
        with open(path, 'r', encoding='UTF-8') as file:
            lines = len(file.readlines())
        print(f"Congratulations, you have recorded {lines} habits.")

    return read_habits_in_file_wrapped

def add_habit_to_dictionary(name_of_dictionary):
    key = input("Enter the habit you made today: ")
    name_of_dictionary[key] = input("Enter the effect of the habit on you: ")
    return key

# Define the directory and ensure it exists
dir_path = r'C:\Users\LENOVO\Desktop\Habits\recording_daily_habits\habits'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

# Define the current date for the filename
timestr = time.strftime("%Y_%m_%d")

# Choice Menu
Choice_Menu = IntEnum('Choice_Menu', ['Dobre_Nawyki', 'Złe_Nawyki', 'Lista_Pomocnicza', 'Wyświetl_nawyki', 'Usuń_nawyk', 'Zakończ'])

good_habits_dict = {}
bad_habits_dict = {}

# Wrapper setup
read_habits_in_file_wrapped = read_habits_and_feedback_wrapper(read_habits_in_file)

while True:
    print("""
        Enter what you did today in terms of your habits:
        Press 1 - Good habits
        Press 2 - Bad habits
        Press 3 - Show helper list
        Press 4 - Show today's habits (from file)
        Press 5 - Remove habit (from file)
        Press 0 - Exit program
        -------------------- """)

    choice = int(input("Enter your choice: "))

    if choice == Choice_Menu.Dobre_Nawyki:
        key = add_habit_to_dictionary(good_habits_dict)
        type_of_habits = "Good_habits_"
        path = create_file_name(type_of_habits, timestr, dir_path)
        open_file_for_safe_habits(path, key)
        read_habits_in_file(path)
        reading_numbered_keys(good_habits_dict)
        print("-" * 30)
        read_habits_in_file_wrapped(path)

    elif choice == Choice_Menu.Złe_Nawyki:
        key = add_habit_to_dictionary(bad_habits_dict)
        type_of_habits = "Bad_habits_"
        path = create_file_name(type_of_habits, timestr, dir_path)
        open_file_for_safe_habits(path, key)
        read_habits_in_file(path)
        reading_numbered_keys(bad_habits_dict)

    elif choice == Choice_Menu.Lista_Pomocnicza:
        print("DAILY GOOD HABITS")
        reading_numbered_keys(daily_good_habits_dictionary)

        print("ELITE HABITS")
        reading_numbered_keys(elite_habits_dictionary)

        print("LEGENDARY HABITS")
        reading_numbered_keys(legendary_habits_dictionary)

    elif choice == Choice_Menu.Wyświetl_nawyki:
        path = create_file_name("Good_habits_", timestr, dir_path)  # Example for good habits
        read_habits_in_file(path)

    elif choice == Choice_Menu.Usuń_nawyk:
        # Add functionality to remove a habit from the file or dictionary
        pass

    elif choice == Choice_Menu.Zakończ:
        break

    else:
        print("Invalid choice, please select a valid option.")