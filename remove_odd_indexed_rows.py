import pandas as pd

def remove_odd_indexed_rows(excel_file_path):
    # Read the Excel file
    df = pd.read_excel(excel_file_path)

    # Remove rows with odd indices (starting from 0)
    df = df.iloc[[i for i in range(len(df)) if i % 2 == 0], :]

    # Save the changes back to the same Excel file
    df.to_excel(excel_file_path, index=False)

    print(f"Rows with odd indices have been successfully removed and saved to {excel_file_path}")

if __name__ == "__main__":
    excel_file_path = "path/to/your/excel_file.xlsx"  # Change this to the path of your Excel file
    remove_odd_indexed_rows(excel_file_path)
