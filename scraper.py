import requests
from bs4 import BeautifulSoup
import streamlit as st

# Define the URL
url = "https://libgen.is/search.php?req=islamic&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all table rows in the HTML
table_rows = soup.find_all("tr")

# Define a list to store the scraped data
data = []

# Extract the data from each table row
for row in table_rows:
    columns = row.find_all("td")
    if len(columns) >= 4:
        book_title = columns[1].text.strip()
        author = columns[2].text.strip()
        year = columns[3].text.strip()
        data.append({"Title": book_title, "Author": author, "Year": year})

# Create a Streamlit app to display the scraped data
st.title("Web Data Scraper")
st.header("Scraped Data")
st.table(data)
