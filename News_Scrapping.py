import requests
from bs4 import BeautifulSoup
import pandas as pd

news_sites = {
    'The Hindu': 'https://www.thehindu.com/',
    'NDTV': 'https://www.ndtv.com/',
    'Indian Express': 'https://indianexpress.com/',
    'India Today': 'https://www.indiatoday.in/',
   
    'Scroll': 'https://scroll.in/'
}

headlines_list = []

for site_name, url in news_sites.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    
    if site_name == 'The Hindu':
        headlines = soup.select('h3',class_="title")  
    elif site_name == 'NDTV':
        headlines = soup.select('h3')
    elif site_name == 'Indian Express':
        headlines = soup.select('h3')
    elif site_name == 'Scroll':
        headlines = soup.select('h1')
    elif site_name == 'India Today':
        headlines = soup.select('h2')


    

    for headline in headlines:
        headlines_list.append({
            'Site': site_name,
            'Headline': headline.get_text(strip=True)
        })

# Save to Excel
df = pd.DataFrame(headlines_list)
df.to_excel('news_headlines.xlsx', index=False)
print("saved Your Data in news_headlines.xlsx File ")
