import json
from prettytable import PrettyTable

def display_data_as_table(data, title):
    table = PrettyTable()
    table.title = title
    if title == "Guesses":
        table.field_names = ["Guess ID", "Numbers"]
        for i, guess in enumerate(data):
            table.add_row([i+1, ", ".join(map(str, guess))])
    else:  # title == "Results"
        table.field_names = ["Result ID", "Numbers"]
        for result_id, numbers in data.items():
            table.add_row([result_id, ", ".join(map(str, numbers))])
    print(table)

def check_results(guesses, results):
    table = PrettyTable()
    table.field_names = ["Result ID", "Guess ID", "Matches", "Matched Numbers"]
    for result_id, result in results.items():
        for i, guess in enumerate(guesses):
            matched_numbers = set(guess) & set(result)
            correct_guesses = len(matched_numbers)
            table.add_row([result_id, i+1, correct_guesses, ", ".join(map(str, matched_numbers))])
    print()
    print(table)

# Specify the absolute path to the data.json file
data_file = r'C:\Users\szeyu\Projects\Mark Six Checker\data.json'

# Load data from file
try:
    with open(data_file, 'r') as f:
        data = json.load(f)
        guesses = data['guesses']
        results = data['results']
except FileNotFoundError:
    guesses = []
    results = {}

while True:
    print("Select a mode:")
    print("1. Terminate")
    print("2. Edit")
    mode = input("Please select: ")
    if mode == "1":
        break
    elif mode == "2":
        display_data_as_table(guesses, "Guesses")
        print()
        display_data_as_table(results, "Results")

        clear_data = input("Clear data? (yes/no): ")
        if clear_data.lower() == "yes":
            guesses = []
            results = {}

        print()
        print("Enter guesses (separated by whitespace, finish with 'd'):")
        while True:
            guess = input()
            if guess.lower() == 'd':
                break
            guesses.append(list(map(int, guess.split())))

        print()
        print("Enter results (format - ID:numbers, finish with 'd'):")
        while True:
            result = input()
            if result.lower() == 'd':
                break
            result_id, numbers = result.split(":")
            results[result_id] = list(map(int, numbers.split()))

        check_results(guesses, results)

        # Save data to file
        with open(data_file, 'w') as f:
            json.dump({'guesses': guesses, 'results': results}, f)

        print()
        print("----------------------------------------------------------------")
        print()