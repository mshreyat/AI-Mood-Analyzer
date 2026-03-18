import pandas as pd
import os

FILE_NAME = "data.csv"

def initialize_csv():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["Date", "Text", "Mood", "ScreenTime"])
        df.to_csv(FILE_NAME, index=False)

def save_entry(text, mood, screen_time):
    """Appends a new entry to the CSV file."""
    from datetime import date
    new_data = {
        "Date": date.today(),
        "Text": text,
        "Mood": mood,
        "ScreenTime": screen_time
    }
    df = pd.read_csv(FILE_NAME)
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

def load_data():
    """Returns the stored data as a Pandas DataFrame."""
    return pd.read_csv(FILE_NAME)