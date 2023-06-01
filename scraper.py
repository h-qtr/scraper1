import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Create a BeautifulSoup object with the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the table element with the search results
    table = soup.find('table', {'class': 'c'})
    # Extract data from the table
    data = []
    rows = table.find_all('tr')
    for row in rows[1:]:  # Exclude the header row
        columns = row.find_all('td')
        title = columns[3].get_text().strip()
        author = columns[1].get_text().strip()
        year = columns[4].get_text().strip()
        data.append({'Title': title, 'Author': author, 'Year': year, 'Publisher': publisher})
    return data

# Set up the Streamlit app
st.title('Web Data Scraper')
url = 'https://libgen.is/search.php?req=topicid69&open=0&column=topic'
data = scrape_data(url)
# Display the scraped data
if data:
    st.table(data)
else:
    st.write('No data found.')

