import pandas as pd
import argparse
import os

def load_data(file_path):
    """Load CSV data into a DataFrame."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean the DataFrame by dropping rows with missing values."""
    return df.dropna()

def analyze_data(df):
    """Perform basic analysis on the DataFrame."""
    print("Credit value counts:")
    print(df['credit'].value_counts())
    
    print("Name value counts:")
    print(df['name'].value_counts())
    
    grouped_df_by_name = df.groupby('name')['credit'].sum().reset_index()
    print("Grouped by name:")
    print(grouped_df_by_name)

def save_cleaned_data(df, output_path):
    """Save the cleaned DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)

def main(input_file, output_file):
    """Main function to execute data analysis."""
    df = load_data(input_file)
    print(df)

    print(df.info())
    print(df.describe())

    df_cleaned = clean_data(df)
    analyze_data(df_cleaned)
    
    save_cleaned_data(df_cleaned, output_file)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("output_file", help="Path to save the cleaned CSV file.")
    
    args = parser.parse_args()
    main(args.input_file, args.output_file)
