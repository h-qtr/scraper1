import requests
from bs4 import BeautifulSoup
import streamlit as st

# Define the URL to scrape
url = 'https://libgen.is/book/index.php?md5=EDA14ED128C9EF556F0D60B270E706D4'

# Make a request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the book details on the page
title = soup.select_one('#main > table.c > tr:nth-child(2) > td:nth-child(2)').text
author = soup.select_one('#main > table.c > tr:nth-child(3) > td:nth-child(2)').text
year = soup.select_one('#main > table.c > tr:nth-child(5) > td:nth-child(2)').text

# Display the scraped data using Streamlit
st.title("Book Details")
st.write(f"Title: {title}")
st.write(f"Author: {author}")
st.write(f"Year: {year}")
