import pandas as pd
import sqlite3

# Read the CSV files
roster_df = pd.read_csv('Roster.csv')
receiving_df = pd.read_csv('Receiving.csv')

# Convert columns to appropriate dtypes (pandas will infer, but we can enforce if needed)
# Optionally, you can specify dtypes manually if you know them, e.g.:
# roster_df = pd.read_csv('Roster.csv', dtype={'Number': int, ...})
# receiving_df = pd.read_csv('Receiving.csv', dtype={'Yards': float, ...})

# Create SQLite database and write tables
conn = sqlite3.connect('mercyhurst_football.db')
roster_df.to_sql('Roster', conn, if_exists='replace', index=False)
receiving_df.to_sql('Receiving', conn, if_exists='replace', index=False)

conn.close()
print('Database created: mercyhurst_football.db with tables Roster and Receiving.')
