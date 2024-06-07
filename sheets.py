import gspread
from google.oauth2 import service_account
import pandas as pd
import os

# Path to the JSON file with Google Sheets credentials
script_directory = os.path.dirname(os.path.abspath(__file__))
credentials_file = os.path.join(script_directory, 'jsw-workbench-78a7024dd97d.json')
# Google Sheets credentials
credentials = service_account.Credentials.from_service_account_file(
    credentials_file, 
    scopes=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
)
def read_from_google_sheet(sheet_title, sheet_name):
    gc = gspread.authorize(credentials)
    try:
        # Open the Google Sheet by its title
        print(f"Trying to open Google Sheet with title: {sheet_title}")
        spreadsheet = gc.open(sheet_title)
        
        # Open the specific sheet by its name
        print(f"Trying to open sheet with name: {sheet_name}")
        worksheet = spreadsheet.worksheet(sheet_name)
        
        # Read data from the sheet into a pandas DataFrame
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        print(df)
        return df
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Spreadsheet with title '{sheet_title}' not found.")
    except gspread.exceptions.WorksheetNotFound:
        print(f"Worksheet with name '{sheet_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_to_google_sheet(df, sheet_title, sheet_name):
    gc = gspread.authorize(credentials)
    try:
        # Open the Google Sheet by its title
        print(f"Trying to open Google Sheet with title: {sheet_title}")
        spreadsheet = gc.open(sheet_title)
        
        # Try to open the specific sheet by its name, or create it if it doesn't exist
        try:
            print(f"Trying to open sheet with name: {sheet_name}")
            worksheet = spreadsheet.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound:
            print(f"Worksheet with name '{sheet_name}' not found. Creating a new one.")
            worksheet = spreadsheet.add_worksheet(title=sheet_name, rows="100", cols="20")
        
        # Write the DataFrame to the sheet
        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("Data written to Google Sheet successfully.")
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Spreadsheet with title '{sheet_title}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_sheets_data():
    # Google Sheet title
    sheet_title = 'Expression_Ressolver'
    # Sheet name within the Google Sheet
    sheet_name = 'Sheet1'

    # Example read operation
    df = read_from_google_sheet(sheet_title, sheet_name)
    if df is not None:
        print("Data read from Google Sheet successfully.")
        return df
    else:
        print("Failed to read data from Google Sheet.")

