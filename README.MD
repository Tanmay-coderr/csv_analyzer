# CSV Data Analyzer

This is a simple Python script that reads, cleans, and analyzes a CSV file containing data. It performs basic analysis, such as showing the count of unique values in specified columns and grouping data by certain columns.

## Features

- Load data from a CSV file.
- Display basic information and statistics about the data.
- Clean the data by removing rows with missing values.
- Group and summarize data.
- Save the cleaned data into a new CSV file.

## Requirements

Before running the script, make sure you have the following installed:

- Python 3.x
- pandas library (for handling data)



To use the script, follow these steps:

1. Clone the repository or download the `csv_analyzer.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located:
   
   cd path/to/your/script/directory
 ##  In this example:

data/test_file.csv is the input CSV file that you want to analyze.
data/cleaned_test_file.csv is the file where the cleaned data will be saved.
Command-Line Arguments
The script takes two arguments:

Input File Path: The path to the input CSV file.
Output File Path: The path to save the cleaned CSV file.
Example CSV File Format
The script expects the CSV file to have a format like this:

name	credit<br>
tanmay	100<br>
rahul	200<br>
sham	300<br>
Script Explanation
The script performs the following tasks:

Load CSV File: Reads a CSV file using the pandas library.
Display Data Info: Prints information about the DataFrame, such as the number of entries, data types, and basic statistics.
Clean Data: Removes rows with missing values.
Analyze Data:
Counts the unique values in the credit and name columns.
Groups the data by name and sums up the credit values.
Save Cleaned Data: Saves the cleaned data into a new CSV file.
4.Now to run the analysis enter the following script
    ```bash             
   python csv_analyzer.py data/test_file.csv data/cleaned_test_file.csv

                  
