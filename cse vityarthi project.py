import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Global variable to hold the DataFrame
df = None
# Define the expected year range for plotting
YEARS = [2015, 2016, 2017, 2018, 2019, 2020]
# List of known car models/columns for easy selection (Based on CAR_SALES.csv mock file)
CAR_MODELS = ['AMAZE', 'JAZZ', 'WR-V', 'CITY', 'CIVIC', 'CR-V', 'HR-V', 'A8', 'Q2', 'Q8', 'RS7', 'KICKS', 'TERRA', 'NANO', 'TIGOR', 'CELERIO X']
# Group the models by manufacturer/type for structured selection in the graph menu
MANUFACTURERS = {
    'HONDA': ['AMAZE', 'JAZZ', 'WR-V', 'CITY', 'CIVIC', 'CR-V', 'HR-V'],
    'AUDI': ['A8', 'Q2', 'Q8', 'RS7'],
    'NISSAN': ['KICKS', 'TERRA'],
    'TATA': ['NANO', 'TIGOR'],
    'MARUTI SUZUKI': ['CELERIO X']
}

def clear_screen():
# For Windows
    if os.name == 'nt':
        os.system('cls')
# For Linux/Mac
    else:
        os.system('clear')

def press_any_key():
    """Waits for user input before continuing."""
    try:
        if sys.version_info[0] < 3:
            raw_input("Press ENTER to continue...")
        else:
            input("Press ENTER to continue...")
    except EOFError:
# Handle case where input is redirected
        print("\nContinuing...")

def read_csv_file(filename):
    """Reads the CSV file into a global DataFrame."""
    global df
    try:
# Read the CSV file, setting the 'MODEL' column as the index
        df = pd.read_csv("C:/Users/Ali/Downloads/car analysis 1.csv", index_col='MODEL')
# Ensure all columns are numeric (sales data)
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            except Exception:
                pass # Keep non-numeric columns as they are
        print(f"\nSuccessfully read {filename}.")
        print(df)
        print(f"\n[{df.shape[0]} rows x {df.shape[1]} columns]")
    except FileNotFoundError:
        print(f"\nERROR: File '{filename}' not found. Please ensure it's in the correct directory.")
    except Exception as e:
        print(f"\nAn error occurred while reading the CSV: {e}")

# --- Data Analysis Menu Functions ---

def show_columns():
    """Displays all column names in the DataFrame."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return
    print("\n2,1- SHOW COLUMNS")
    print(df.columns)

def show_top_rows():
    """Displays the first N rows."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return
    print("\n2,2- SHOW TOP ROWS")
    try:
        n = int(input("Enter Total rows you want to show: "))
        if n < 0:
            print("Please enter a positive number.")
            return
        print(df.head(n))
        print(f"\n[{df.head(n).shape[0]} rows x {df.shape[1]} columns]")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_bottom_rows():
    """Displays the last N rows."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return
    print("\n2,3- SHOW BOTTOM ROWS")
    try:
        n = int(input("Enter Total rows you want to show: "))
        if n < 0:
            print("Please enter a positive number.")
            return
        print(df.tail(n))
        print(f"\n[{df.tail(n).shape[0]} rows x {df.shape[1]} columns]")
    except ValueError:
        print("Invalid input. Please enter a number.")

def show_specific_column():
    """Displays the values of a user-specified column."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return
    print("\n2,4- SHOW PARTICULAR COLUMN")
    print("Available columns:")
    print(df.columns.values)
    column_name = input("Enter Column Name that You want to print: ").strip().upper()

    if column_name in df.columns:
        print(df[column_name])
    else:
        print(f"Column '{column_name}' not found.")

def add_new_record():
    """Adds a new car model/column to the DataFrame."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return
    print("\n2,5- ADD A NEW RECORD (Car Model)")
    new_model_name = input("Enter New Model Name: ").strip().upper()

    if new_model_name in df.columns:
        print(f"Model '{new_model_name}' already exists.")
        return

    sales_data = {}
    valid_data = True
    for year in YEARS:
        while True:
            try:
                # The index names in the provided image are 'APPL. SALES IN 2015', etc.
                prompt = f"Enter Sales in {year}: "
                sales = int(input(prompt).strip())
                sales_data[f"APPL. SALES IN {year}"] = sales
                break
            except ValueError:
                print("Invalid input. Sales must be a whole number.")

# Create a new Series to be appended as a column
    new_column = pd.Series(sales_data, name=new_model_name)
    
# Align the index of the new Series to the existing DataFrame index
# (Since the index is the sales years string, this is crucial)
    df[new_model_name] = new_column
    
# Update the global list of car models and manufacturers
    if new_model_name not in CAR_MODELS:
        CAR_MODELS.append(new_model_name)
# Assuming new model is generic until user specifies manufacturer
        MANUFACTURERS['OTHER'] = MANUFACTURERS.get('OTHER', []) + [new_model_name]

    print(f"\nSuccessfully added model '{new_model_name}'.")
    print(df)
    print(f"\n[{df.shape[0]} rows x {df.shape[1]} columns]")


def delete_column():
    """Deletes a user-specified column (car model) from the DataFrame."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return
    print("\n2,6- DELETE A COLUMN (Car Model)")
    print("Available columns:")
    print(df.columns.values)
    column_name = input("Enter column Name to delete :").strip().upper()

    if column_name in df.columns:
        df.drop(columns=[column_name], inplace=True)
        print(f"\nSuccessfully deleted column '{column_name}'.")
        print(df)
        print(f"\n[{df.shape[0]} rows x {df.shape[1]} columns]")
# Optionally update CAR_MODELS list, though it's less critical for functionality
        try:
            CAR_MODELS.remove(column_name)
            for key in MANUFACTURERS:
                if column_name in MANUFACTURERS[key]:
                    MANUFACTURERS[key].remove(column_name)
        except ValueError:
            pass
# Model might not have been in the initial list
    else:
        print(f"Column '{column_name}' not found.")

def data_summary():
    """Displays descriptive statistics (summary) of the numeric columns."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return
    print("\n2,7- DATA SUMMARY")
# Tidy up the output to match the screenshot format
    summary_df = df.describe().transpose()
# Format the numerical output for better readability
    pd.set_option('display.float_format', '{:.4f}'.format)
    print(summary_df)
    print(f"\n[{summary_df.shape[0]} rows x {summary_df.shape[1]} columns]")
    pd.reset_option('display.float_format') # Reset the float format

# --- Graph Menu Functions ---

def plot_graph(model, graph_type='line'):
    """Generates a line or bar graph for a single car model."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return

    if model not in df.columns:
        print(f"Model '{model}' not found in data.")
        return

# Extract sales data for the selected model
    sales_data = df[model].values
    
# Create the figure and axes
    plt.figure(figsize=(10, 6))
    
# Define title components
    manufacturer = [m for m, models in MANUFACTURERS.items() if model in models]
    manufacturer = manufacturer[0] if manufacturer else "UNKNOWN"
    
    plt.title(f"{manufacturer}- {model}")
    
# Determine plot type
    if graph_type == 'line':
        plt.plot(YEARS, sales_data, marker='o', linestyle='-', color='b')
        plt.title(f"Car Wise Sales Count (Line Graph) - {manufacturer}- {model}")
    elif graph_type == 'bar':
        plt.bar(YEARS, sales_data, color='skyblue')
        plt.title(f"Company wise sales count (Bar Graph) - {manufacturer}- {model}")

# Set common labels and grid
    plt.xlabel("Year")
    plt.ylabel("Total Sales")
    plt.xticks(YEARS)
    plt.grid(True)
    plt.show()

def graph_menu():
    """Handles the sub-menu for generating graphs."""
    global df
    if df is None:
        print("\nData not loaded. Please read the CSV file first (Option 1 in Main Menu).")
        return

    while True:
        clear_screen()
        print("3. GRAPH MENU")
        print("------------------------------")
        print("1. Car Wise Line Graph")
        print("2. Car Wise Bar Graph")
        print("3. Exit (Move to main menu)")
        print("\nAvailable Manufacturers/Groups:")
        for i, (mfg, models) in enumerate(MANUFACTURERS.items()):
            print(f"  {i+1}. {mfg} ({', '.join(models)})")
        print("------------------------------")
        
        choice = input("Enter your choice: ").strip()

        if choice == '5':
            break

        if choice not in ['1', '2','3','4']:
            print("Invalid choice. Please try again.")
            press_any_key()
            continue
        
        graph_type = 'line' if choice == '1' else 'bar'
        
# Manufacturer selection
        print("\nSelect a Manufacturer to see available models:")
        
        mfg_choice = input("Enter Manufacturer choice number: ").strip()
        try:
            mfg_index = int(mfg_choice) - 1
            manufacturer_name = list(MANUFACTURERS.keys())[mfg_index]
            available_models = MANUFACTURERS[manufacturer_name]
        except (ValueError, IndexError):
            print("Invalid manufacturer selection. Returning to Graph Menu.")
            press_any_key()
            continue
        
        print(f"\nAvailable {manufacturer_name} Models:")
        for i, model in enumerate(available_models):
            print(f"  {i+1}. {model}")
        
# Model selection
        model_choice = input("Enter Car Model choice number: ").strip()
        try:
            model_index = int(model_choice) - 1
            selected_model = available_models[model_index]
            
            # Generate the plot
            plot_graph(selected_model, graph_type)
            press_any_key()
            
        except (ValueError, IndexError):
            print("Invalid model selection.")
            press_any_key()
            
# --- Main Menu Functions ---

def data_analysis_menu():
    """Handles the sub-menu for data analysis operations."""
    while True:
        clear_screen()
        print("2. DATA ANALYSIS MENU")
        print("---------------------")
        print("Data Analysis MENU")
        print("1. Show Columns")
        print("2. Show Top Rows")
        print("3. Show Bottom Rows")
        print("4. Show Specific Column")
        print("5. Add a New Record")
        print("6. Delete a Column")
        print("7. Data Summary")
        print("8. Exit (Move to main menu)")
        print("---------------------")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            show_columns()
        elif choice == '2':
            show_top_rows()
        elif choice == '3':
            show_bottom_rows()
        elif choice == '4':
            show_specific_column()
        elif choice == '5':
            add_new_record()
        elif choice == '6':
            delete_column()
        elif choice == '7':
            data_summary()
        elif choice == '8':
            break
        else:
            print("\nInvalid choice. Please select an option from 1 to 8.")

        press_any_key()


def main_menu():
    """Displays the main application menu and handles top-level navigation."""
    global df
    print("Welcome to the Car Sales Data Analyzer")
    
# Attempt to load the data immediately if the mock file exists, for convenience
    if os.path.exists("C:/Users/Ali/Downloads/car analysis 1.csv"):
        print("Attempting to load 'CAR_SALES.csv' automatically...")
        read_csv_file("C:/Users/Ali/Downloads/car analysis 1.csv")
        press_any_key()
    else:
        print("NOTE: 'CAR_SALES.csv' not found. Please select option 1 or create the file using the mock content.")
    
    while True:
        clear_screen()
        print("OUTPUTS")
        print("MAIN MENU")
        print("------------------------------")
        print("MAIN MENU")
        print("1. Read CSV File")
        print("2. Data Analysis Menu")
        print("3. Graph Menu")
        print("4. Exit")
        print("------------------------------")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
# This is the point where the user would specify the file name
            filename = input("Enter CSV file name (e.g., CAR_SALES.csv): ").strip()
            if not filename:
                 filename = "CAR_SALES.csv"
            read_csv_file(filename)
        elif choice == '2':
            if df is not None:
                data_analysis_menu()
            else:
                print("\nData not loaded. Please read the CSV file first (Option 1).")
        elif choice == '3':
            if df is not None:
                graph_menu()
            else:
                print("\nData not loaded. Please read the CSV file first (Option 1).")
        elif choice == '4':
            print("\nExiting the application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select an option from 1 to 4.")

        press_any_key()

if __name__ == "__main__":
# Check for required libraries
    try:
        import pandas as pd
        import matplotlib.pyplot as plt
    except ImportError:
        print("ERROR: This script requires 'pandas' and 'matplotlib'.")
        print("Please install them using: pip install pandas matplotlib")
        sys.exit(1)
        
    main_menu()
