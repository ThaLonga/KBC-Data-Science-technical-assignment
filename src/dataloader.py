import pandas as pd

def read_xlsx(file_path):
    # Read the entire Excel file, skipping the first sheet
    sheet_names = pd.ExcelFile(file_path).sheet_names
    if len(sheet_names) < 5:
        raise ValueError("The Excel file does not contain at least 5 sheets.")
    
    # Skip the first sheet and read the remaining sheets into DataFrames
    sheets_to_read = sheet_names[1:5]
    df_list = [pd.read_excel(file_path, sheet_name=sheet) for sheet in sheets_to_read]
    
    # Assign each DataFrame to the respective variable
    soc_dem, products, in_out, sales = df_list
    
    return soc_dem, products, in_out, sales

# Example usage:
# soc_dem, products, in_out, sales = read_xlsx("file.xlsx")
