import pandas as pd
import scraper.py as sc

# Run the scraper

# Leer los ultimos datos del csv del scraper
base= pd.read_csv('base.csv', header=0)

# Read the latest scrape and compare against the database to see the new and old ones
df = pd.read_csv('results.cs', header = 0)
base = pd.read_sql(query)

new = df[~df['boletin'].isin(base['boletin'])]
print(new.head(10))



