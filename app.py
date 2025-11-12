import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from shiny import App, render, ui, reactive

df = pd.read_csv('attendance_anonymised-1.csv')
df = df.drop("Planned End Date", axis=1) # Drops Planned End Date, axis=1 means it drops a column
df = df.rename(columns={'Person Code': 'Person Code', 'Unit Instance Code': 'Module Code', 'Calocc Code': 'Year', 
                   'Surname': 'Surname', 'Forename': 'Forename', 'Long Description': 'Module Name', 'Register Event ID': 'Event ID',
                   'Object ID': 'Object ID', 'Register Event Slot ID': 'Event Slot ID', 'Planned Start Date': 'Date', 
                   'is Positive': 'Has Attended', 'Postive Marks': 'Attended', 'Negative Marks': 'NotAttended',
                   'Usage Code': 'Attendance Code'}) # Rename method to change column names
df['Date'] = pd.to_datetime(df['Date']) # Datetime method on 'Date' column
Module_Names = df['Module Name'].unique().tolist() # Provides a list of unique values in the column 'Module Name' and puts them into a list

# UI
app_ui = ui.page_fluid(
    ui.panel_title('Module Picker')
)




# Server
def server(input, output, session):


app = App(app_ui, server)

if __name__ == "__main__":
    app.run() 