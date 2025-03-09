import requests
from bs4 import BeautifulSoup
import pandas as pd

# Flipkart laptops URL
url = "https://www.flipkart.com/search?q=laptops"

# Headers to act like a real browser
headers = {"User-Agent": "Mozilla/5.0"}

# Send a GET request
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract product details
laptop_names = [item.text for item in soup.find_all("div", class_="_4rR01T")]
laptop_prices = [price.text for price in soup.find_all("div", class_="_30jeq3")]

# Store data in a DataFrame
df = pd.DataFrame({"Laptop Name": laptop_names, "Price": laptop_prices})

# Save as CSV
df.to_csv("laptops.csv", index=False)

print("Scraping Complete! Data saved as laptops.csv")
