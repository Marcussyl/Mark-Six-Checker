# Mark-Six-Checker

This is a Python application that allows users to store and check their Mark Six lottery guesses against actual results. The application stores the data in a JSON file and displays the data and results in a tabular format.

## Requirements

- Python 3.6 or higher
- prettytable module

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python modules with the following command:

```bash
pip install prettytable
```

## Usage

1. Run the Python script with the following command:

    ```bash
    python mark_six_checker.py
    ```

2. The application will display the stored guesses and results in a tabular format.
3. Select a mode:
    Enter "1" to terminate the application.
    Enter "2" to edit the data.
4. If you selected mode "2", the application will ask if you want to clear the data. Enter "yes" to clear the data or "no" to keep the data.
5. Enter your guesses. Each guess should be a series of numbers separated by whitespace.    Finish entering guesses by typing 'd'.
6. Enter the results. Each result should be in the format "ID:numbers". Finish entering results by typing 'd'.
7. The application will display the matches between your guesses and the results in a tabular format.
8. The application will save the guesses and results to a JSON file in the same directory as the script.

## Workflow

1. The user runs the script.
2. The script loads the stored guesses and results from a JSON file.
3. The script displays the stored guesses and results in a tabular format.
4. The user selects a mode.
5. If the user selected mode "2", the script allows the user to edit the data.
6. The user enters their guesses and the results.
7. The script checks the matches between the guesses and the results and displays the matches in a tabular format.
8. The script saves the guesses and results to the JSON file.
9. The script repeats from step 3 until the user selects mode "1" to terminate the application.
