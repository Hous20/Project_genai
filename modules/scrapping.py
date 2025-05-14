# Search for basketball articles in English Wikipedia and save them to a structured CSV

import os
import pandas as pd
import re
import requests
import time
from tqdm import tqdm
from typing import List, Dict
from bs4 import BeautifulSoup

# Define the output CSV file path
output_csv_path = "data/wikipedia_basketball_articles.csv"

# Create the output directory if it doesn't exist
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

# Wikipedia API endpoint and parameters
api_url = "https://en.wikipedia.org/w/api.php"
search_params = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": "basketball",
    "srlimit": 1000  # Adjust the number of results as needed
}

# Function to get article content
def get_article_content(page_id):
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": 0,
        "explaintext": 1,
        "pageids": page_id
    }
    
    response = requests.get(api_url, params=params)
    result = response.json()
    
    try:
        page_data = result["query"]["pages"][str(page_id)]
        title = page_data["title"]
        content = page_data["extract"]
        return title, content
    except Exception as e:
        print(f"Error retrieving content for page {page_id}: {e}")
        return None, None

# Initialize an empty list to store the data
data = []

# Search for articles
response = requests.get(api_url, params=search_params)
search_results = response.json()

# Extract article information
for result in tqdm(search_results["query"]["search"]):
    title, content = get_article_content(result["pageid"])
    
    if title and content:
        # Clean the content
        content = re.sub(r"\n+", "\n", content)  # Remove extra newlines
        content = re.sub(r"\s+", " ", content)   # Remove extra spaces
        
        # Add to our data collection
        data.append({
            "title": title,
            "pageid": result["pageid"],
            "content": content
        })
        
        # Be gentle to Wikipedia's servers
        time.sleep(1)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(output_csv_path, index=False, encoding="utf-8")
print(f"Saved {len(data)} articles to {output_csv_path}")