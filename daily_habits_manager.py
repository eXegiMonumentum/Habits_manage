import os
import time
from enum import IntEnum

# Słowniki z nawykami
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


# Funkcja do tworzenia folderu 'habits' jeśli nie istnieje
def create_habits_folder():
    habits_folder = 'habits'
    if not os.path.exists(habits_folder):
        os.makedirs(habits_folder)
    return habits_folder


# Funkcja do zapisania nawyku w pliku
def open_file_for_safe_habits(path, key):
    with open(path, 'a+', encoding="UTF-8") as file:
        file.write(key)
        file.write('\n')


# Funkcja do tworzenia nazwy pliku
def create_file_name(type_of_habits, timestr, dir_path):
    part_of_path = type_of_habits + timestr + ".txt"
    file_full_path = os.path.join(dir_path, part_of_path)
    return file_full_path


# Funkcja do wyświetlania nawyków
def read_habits_in_file(path):
    with open(path, 'r', encoding="UTF-8") as file:
        if "Good" in path:
            print("\n", "GOOD Habits")
        else:
            print("\n", "BAD HABITS")
        print(file.read())


# Funkcja do dodawania nawyku do słownika
def add_habit_to_dictionary(name_of_dictionary):
    key = input("Enter the habit you made today: ")
    name_of_dictionary[key] = input("Enter the effect of the habit on you: ")
    return key


# Funkcja do usuwania nawyku z pliku
def remove_habit_from_file(path, habit):
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            lines = file.readlines()

        # Otwórz plik ponownie do zapisu i przekaż tylko te linie, które nie zawierają nawyku
        with open(path, 'w', encoding="UTF-8") as file:
            for line in lines:
                if habit not in line:  # Pomijaj linie, które zawierają nawyk
                    file.write(line)
        print(f"'{habit}' has been removed from the file.")
    except FileNotFoundError:
        print("File not found. Nothing to remove.")


# Funkcja do usuwania nawyku ze słownika
def remove_habit_from_dictionary(habit, type_of_habit):
    if type_of_habit == "Good":
        if habit in good_habits_dict:
            del good_habits_dict[habit]
            print(f"'{habit}' has been removed from good habits.")
        else:
            print(f"'{habit}' not found in good habits.")
    elif type_of_habit == "Bad":
        if habit in bad_habits_dict:
            del bad_habits_dict[habit]
            print(f"'{habit}' has been removed from bad habits.")
        else:
            print(f"'{habit}' not found in bad habits.")


# Define the current date for the filename
timestr = time.strftime("%Y_%m_%d")

# Inicjalizacja słowników nawyków
good_habits_dict = {}
bad_habits_dict = {}

# Tworzymy folder na nawyki
habits_folder = create_habits_folder()

# Menu wyboru
Choice_Menu = IntEnum('Choice_Menu',
                      ['Good_Habits', 'Bad_Habits', 'Show_List', 'Show_Todays_Habits', 'Remove_Habit', 'Exit'])

# Główna pętla programu
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

    if choice == Choice_Menu.Good_Habits:
        key = add_habit_to_dictionary(good_habits_dict)
        type_of_habits = "Good_habits_"
        path = create_file_name(type_of_habits, timestr, habits_folder)
        open_file_for_safe_habits(path, key)
        read_habits_in_file(path)
        print("-" * 30)

    elif choice == Choice_Menu.Bad_Habits:
        key = add_habit_to_dictionary(bad_habits_dict)
        type_of_habits = "Bad_habits_"
        path = create_file_name(type_of_habits, timestr, habits_folder)
        open_file_for_safe_habits(path, key)
        read_habits_in_file(path)
        print("-" * 30)

    elif choice == Choice_Menu.Show_List:
        print("DAILY GOOD HABITS")
        for habit in daily_good_habits_dictionary:
            print(f'{habit} - {daily_good_habits_dictionary[habit]}')

        print("ELITE HABITS")
        for habit in elite_habits_dictionary:
            print(f'{habit} - {elite_habits_dictionary[habit]}')

        print("LEGENDARY HABITS")
        for habit in legendary_habits_dictionary:
            print(f'{habit} - {legendary_habits_dictionary[habit]}')

    elif choice == Choice_Menu.Show_Todays_Habits:
        print("\nToday's Good Habits:")
        path = create_file_name("Good_habits_", timestr, habits_folder)  # Example for good habits
        read_habits_in_file(path)
        print("\nToday's Bad Habits:")
        path = create_file_name("Bad_habits_", timestr, habits_folder)  # Example for bad habits
        read_habits_in_file(path)
        print("-" * 30)

    elif choice == Choice_Menu.Remove_Habit:
        print("Enter the habit you want to remove:")
        habit_to_remove = input("Habit name: ")

        # Wybierz, czy to dobry, czy zły nawyk
        print("Is this a good habit or a bad habit?")
        print("Press 1 for Good, 2 for Bad")
        habit_type = int(input())

        # Usuwanie z odpowiedniego słownika
        if habit_type == 1:
            remove_habit_from_dictionary(habit_to_remove, "Good")
            path = create_file_name("Good_habits_", timestr, habits_folder)
            remove_habit_from_file(path, habit_to_remove)
        elif habit_type == 2:
            remove_habit_from_dictionary(habit_to_remove, "Bad")
            path = create_file_name("Bad_habits_", timestr, habits_folder)
            remove_habit_from_file(path, habit_to_remove)
        else:
            print("Invalid option.")
        print("-" * 30)

    elif choice == Choice_Menu.Exit:
        break

    else:
        print("Invalid choice, please select a valid option.")
