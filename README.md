# 🚗 Car Sales Data Analyzer: Project

This document provides an overview, feature list, setup instructions, and testing guidelines for the Car Sales Data Analyzer project.
## 🚀 About Me
Name-seru ganesh



## 🧑‍💻 Features

- The application is structured into a Main Menu, a Data Analysis Menu, and a Graph Menu, offering the following capabilities:
## 1. Main Menu
- Read CSV File: Load car sales data from a user-specified CSV file into a pandas DataFrame.
- Navigate: Access the Data Analysis Menu or the Graph Menu.
## 2. Data Analysis Menu
- Show Columns: Display all column names (car models) in the dataset.
- 	Show Top/Bottom Rows: View a specified number of rows from the beginning or end of the dataset.
- 	Show Specific Column: Print the sales data for a single, user-selected column/car model.
- 	Add a New Record (Car Model): Interactively prompt the user for a new car model name and its sales figures for the years 2015-2020, adding it as a new column to the DataFrame.
- 	Delete a Column (Car Model): Remove a specified car model column from the DataFrame.
- 	Data Summary: Display descriptive statistics (e.g., count, mean, std) of all numeric columns.
## 3. Graph Menu
-  Car Wise Line Graph: Generate a line plot showing the sales trend for a selected car model over the years (2015-2020).
- Car Wise Bar Graph: Generate a bar chart illustrating the sales count for a selected car model per year (2015-2020).
- 	Structured Selection: Models are grouped by manufacturer (e.g., HONDA, AUDI, NISSAN, TATA, MARUTI SUZUKI, OTHER) for simplified model selection.



## 🪜 Steps to Install & Run the Project
-  Prerequisites
Ensure you have Python 3 installed on your system.
-  Install Dependencies
The project requires the pandas and matplotlib libraries. You can install them using pip:
Bash
pip install pandas matplotlib
-  Create a Data File
The script expects a CSV file to work with, typically named car analysis 1.csv as referenced in the code, or a name provided by the user. The file must have a column named MODEL (as the index) and columns representing sales years for 2015 to 2020 (e.g., APPL. SALES IN 2015).
-  Run the Script
Execute the project file from your terminal:
Bash
python "cse vityarthi project.py"
The application will launch the MAIN MENU. If the script attempts to load a file automatically and fails, select option 1. Read CSV File and enter the name of your data file.

## ⚙️Technologies/Tools Used
- Language: Python 3.14
- 	Data Manipulation: pandas
- 	Data Visualization: matplotlib.pyplot
- 	Environment: Console/Terminal (IDLE Shell 3.14.0)

## 🧪 Instructions for Testing
##	Initial Load Test:
 - Start the application.
 - Select 1. Read CSV File and load your data file.
## Data Analysis Testing (Option 2):
- Enter the Data Analysis Menu.
- 	Test 5. Add a New Record: Add a new model, e.g., HUMMER, with sales data, and verify the successful addition. Note how the system handles invalid input (e.g., non-whole number for sales).
- Test 8. Exit to return to the main menu.
## 	Graph Testing (Option 3):
- Enter the Graph Menu.
- 	Select 1. Car Wise Line Graph.
- 	Select a manufacturer (e.g., 2. AUDI).
- 	Select a model (e.g., A8).
- 	Verify that a line graph window appears showing the sales trend for the selected model.
- 	Repeat the process for 2. Car Wise Bar Graph.
 ## Screenshots
<img width="1651" height="1126" alt="Screenshot 2025-11-24 125533" src="https://github.com/user-attachments/assets/9cd86cba-5129-4560-8add-5be30038c0ab" />
<img width="1055" height="693" alt="Screenshot 2025-11-24 125652" src="https://github.com/user-attachments/assets/33cd61b9-b0c3-43c7-9438-3e1f0fc5660d" />
<img width="1697" height="961" alt="Screenshot 2025-11-24 125744" src="https://github.com/user-attachments/assets/a9e37e06-6c58-4935-adb2-2300af7f6999" />
<img width="1733" height="930" alt="Screenshot 2025-11-24 125915" src="https://github.com/user-attachments/assets/8f5480fe-0e66-44b9-a768-41dd44fe0e1a" />
