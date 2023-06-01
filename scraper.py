import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to scrape data from the URL
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extracting the title
    title = soup.find('h1', {'class': 'headline'}).text.strip()
    
    # Extracting the article content
    article = soup.find('div', {'class': 'article-body'})
    paragraphs = article.find_all('p')
    content = '\n'.join([p.text for p in paragraphs])
    
    return title, content

# Streamlit web application
def main():
    st.title("Web Data Scraper")
    url = st.text_input("Enter URL", "https://www.foxnews.com/politics/house-passes-mccarthy-biden-debt-ceiling-deal-sends-senate-five-days-funding-crunch")
    if st.button("Scrape"):
        title, content = scrape_data(url)
        st.subheader(title)
        st.write(content)

if __name__ == '__main__':
    main()
